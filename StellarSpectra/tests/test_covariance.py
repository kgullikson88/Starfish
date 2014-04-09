import pytest
from StellarSpectra.spectrum import *
import numpy as np
from StellarSpectra.covariance import *
import StellarSpectra.constants as C

class TestCCovarianceMatrix:
    def setup_class(self):
        self.dataspectrum = DataSpectrum.open("tests/WASP14/WASP-14_2009-06-15_04h13m57s_cb.spec.flux", orders=np.array([21,22,23]))
        self.cov = CovarianceMatrix(self.dataspectrum, 1)

    def test_bad_update(self):

        with pytest.raises(C.ModelError) as e:
            self.cov.update({"sigAmp":1, "logAmp":0, "l":-1})
        print(e.value)

    def test_update(self):
        self.cov.update({"sigAmp":1, "logAmp":0, "l":1})

    def test_evaluate(self):
        lnprob = self.cov.evaluate(self.dataspectrum.fls[1])
        print(lnprob)

    def test_one_order(self):
        dataspectrum = DataSpectrum.open("tests/WASP14/WASP-14_2009-06-15_04h13m57s_cb.spec.flux", orders=np.array([22]))
        cov = CovarianceMatrix(dataspectrum, 0)
        cov.update({"sigAmp":1, "logAmp":0, "l":1})
        lnprob = cov.evaluate(self.dataspectrum.fls[0])
        print(lnprob)