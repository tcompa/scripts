'''
program: sort_bibtex.py
created: 2016-05-25 -- 19 CEST
author: tc

This script parses a bibtex file and then rewrites it in a sorted way.
WARNING: comments should start with #.
'''

import os
import shutil
import sys
import time
import subprocess


def ask_confirmation(prompt=None, default_response=False):
    '''
    Taken from:
    http://code.activestate.com/recipes/541096-prompt-the-user-for-confirmation

    Prompts for yes/no response from the user, and returns True/False.

    Input:
      + prompt         : the message to show (string)
      + default_resp   : default answer, if user only types 'enter' (boolean)
    '''

    if prompt is None:
        prompt = 'Confirm'

    if default_response:
        prompt = '%s [%s]|%s: ' % (prompt, 'y', 'n')
    else:
        prompt = '%s [%s]|%s: ' % (prompt, 'n', 'y')

    while True:
        ans = raw_input(prompt)
        if not ans:
            return default_response
        if ans not in ['y', 'Y', 'n', 'N']:
            print 'please enter y or n.'
            continue
        if ans == 'y' or ans == 'Y':
            return True
        if ans == 'n' or ans == 'N':
            return False


def temporary_backup(filename):
    assert filename.endswith('.bib'), 'ERROR: %s is not a bib file.' % filename
    tmpdir = '/tmp/tmp_backups_bibtex/'
    try:
        assert os.path.isdir(tmpdir)
    except AssertionError:
        os.makedirs(tmpdir)
    tmpcopy = tmpdir + time.strftime("%Y%m%d-%H_%M_%S") + '_' + filename
    shutil.copy(filename, tmpcopy)
    print 'Copied %s to %s.' % (filename, tmpcopy)
    return tmpcopy


def recognize_line(_line, _iline):
    condition_start_1 = _line[0] == '@' and _line[-1] == ','
    condition_start_2 = '{' in _line and '}' not in _line
    if condition_start_1 and condition_start_2:
        return 'start_line'
    elif _line.replace(' ', '') == '}':
        return 'end_line'
    elif '=' in _line:
        return 'mid_line'
    elif _line[0] == '#':
        return 'comment'
    else:
        errmsg = 'ERROR: could not recognize line %i: "%s"\n' % (_iline, _line)
        errmsg += '(possible explanation: comments should start with #)'
        sys.exit(errmsg)


def call_bash_command(cmdlist, Verbose=False):
    '''
    Call a bash command and catch its returncode, stdout, and stderr.
    '''
    p = subprocess.Popen(cmdlist, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()
    if Verbose:
        print '*' * 80
        print '[call_bash_command] start'
        print 'returncode:'
        print p.returncode
        print 'stdout:'
        print stdout
        print 'stderr:'
        print stderr
        print '[call_bash_command] end'
        print '*' * 80
    return p.returncode, stdout, stderr


def write_git_revision_hash(output):
    commands = ['git', 'rev-parse', 'HEAD']
    returncode, stdout, stderr = call_bash_command(commands, Verbose=False)
    if returncode == 0:
        git_hash = stdout.replace('\n', '')
        output.write('# Current git hash %s\n' % git_hash)
    else:
        print 'WARNING: could not find a git hash.'


def store_bibtex(_db, _file_output, _backup):
    out = open(_file_output, 'w')
    out.write('# Automatically generated (%s)' %
              time.strftime("%Y-%m-%d - %H:%M:%S"))
    out.write(' using sort_bibtex.py.\n')
    write_git_revision_hash(out)
    out.write('# Temporary backup of the original file: %s.\n' % _backup)
    out.write('\n')
    for item_type in sorted(_db.keys()):
        out.write('#' * 80 + '\n')
        out.write('# %s section:\n\n' % item_type)
        sorted_IDs = sorted(_db[item_type].keys())
        for ID in sorted_IDs:
            out.write('@%s{%s,\n' % (item_type, ID))
            assert ID in _db[item_type].keys()
            for line in _db[item_type][ID]:
                out.write(line + '\n')
            out.write('}\n')
            out.write('\n')
    out.close()


# input file
if len(sys.argv) != 2:
    sys.exit('ERROR: missing argument.')
file_input = sys.argv[1]
assert os.path.isfile(file_input)
assert file_input.endswith('.bib')

# temporary backup
backup_file = temporary_backup(file_input)

# read file
with open(file_input) as f:
    lines = f.read().splitlines()

# initialization
db = {}
allowed_items = {'article', 'book', 'phdthesis', 'incollection', 'unpublished',
                 'misc'}
comment_lines = []

# main loop
InsideItem = False
for iline, line in enumerate(lines):

    if len(line.replace(' ', '').replace('\t', '')) == 0:
        continue

    if '\t' in line:
        sys.exit('ERROR: tab in line %i, please fix it.' % iline)

    line_type = recognize_line(line, iline)
    if line_type == 'start_line':
        # Set InsideItem lock
        if InsideItem:
            sys.exit('ERROR (line %i): start_line in previous item.' %
                     line_type)
        InsideItem = True
        # Get item_type and ID
        type_and_ID = line.replace(' ', '').replace('@', '').replace(',', '')
        item_type, ID = type_and_ID.split('{')
        if item_type != item_type.lower():
            sys.exit('FIXME: non lower-case itemtype at line %i.' % iline)
        if item_type not in allowed_items:
            sys.exit('ERROR (%i): itemtype %s not known.' % (iline, item_type))
        # Update database
        if item_type not in db.keys():
            db[item_type] = {}
        if ID in db[item_type]:
            sys.exit('FIXME: duplicate item at line %i.' % iline)
        db[item_type][ID] = []

    elif line_type == 'mid_line':
        # Update database
        db[item_type][ID].append(line)

    elif line_type == 'end_line':
        # Release InsideItem lock
        InsideItem = False

    elif line_type == 'comment':
        comment_lines.append(line)

    else:
        sys.exit('ERROR: something wrong with line %i.' % iline)

print
print 'COMMENTS'
print 'The following comments will be removed:'
for line in comment_lines:
    if len(line.replace('#', '')) == 0:
        continue
    print ' ', line
print
print 'SUMMARY'
for item_type in sorted(db.keys()):
    print item_type
    print len(db[item_type])
    os.system('grep -i "%s{" %s | wc -l' % (item_type, file_input))

print
message = 'Check above, COMMENTS and SUMMARY'
message += ' (for each item type, the two numbers should be the same).'
message += '\nDoes it look OK? '
message += 'Can I *overwrite* %s?' % file_input
overwwrite = ask_confirmation(message, default_response=False)
if overwwrite:
    print 'Now overwriting (temporary backup: %s).' % backup_file
    store_bibtex(db, file_input, backup_file)
else:
    print 'Not doing anything. Ciao.'
