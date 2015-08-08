import numpy
import math
import sys
from matplotlib import pyplot

def err_indept(obs):
    N = len(obs)
    av  = sum(obs) / float(N)
    av2 = sum(i ** 2 for i in obs) / float(N)
    return math.sqrt((av2 - av ** 2) / float(N))

def bunching(obs, list_lbin, namevar, datafile, plotname, DoPlot=True):
    list_lbin = [i for i in list_lbin if 10 * i < len(obs)]
    old_list = []
    new_list = numpy.array(obs).tolist()
    n_lbin = len(list_lbin)
    list_fact = [1] + [list_lbin[i + 1] / list_lbin[i] for i in xrange(n_lbin - 1)]
    list_err = []
    for l in xrange(n_lbin):
       fact = list_fact[l]
       old_list = new_list
       new_list = []
       size = len(old_list)
       while size > fact:
          x = sum(old_list.pop() for i in range(fact))
          new_list.append(x * 1.0 / fact)
          size -= fact
       err = err_indept(new_list)
       list_err.append(err)
    f = open(datafile,"w")
    f.write('# nsteps = '+str(len(obs))+'\n')
    f.write('# list_lbin = '+str(list_lbin)+'\n')
    f.write('# list_err  = '+str(list_err)+'\n')
    numpy.savetxt(f, numpy.array([list_lbin, list_err]).T)
    f.close()

    if DoPlot:
        pyplot.clf()
        pyplot.semilogx(list_lbin,list_err,'bo-',ms=10)
        pyplot.xlabel('bin length',fontsize=18)
        pyplot.ylabel('error '+namevar,fontsize=18)
        pyplot.savefig(plotname, bbox_inches='tight')
        pyplot.clf()

    return [list_lbin, list_err, numpy.mean(numpy.array(obs))]

# returns zero if the error has not saturated
def look_for_err(l_err):
    for i in xrange(len(l_err) - 1):
        if l_err[i] > l_err[i + 1]:
            return l_err[i]
    return 0.0

datafile = sys.argv[1]

obs = numpy.loadtxt(datafile)
list_lbin = [2 ** k for k in xrange(20)]
[l_lbin, l_err, obs_av] = bunching(obs, list_lbin, '', 'bins-%s' % datafile, 'plot-bins-%s.png' % datafile)
err_av = look_for_err(l_err)

print 'average: %f +/- %f' % (obs_av, err_av)
print '(gaussian error: %f)' % l_err[0]
