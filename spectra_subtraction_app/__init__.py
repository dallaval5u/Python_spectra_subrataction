from spectra_subtraction_app.datahandler import RegionsCollection, Region
from spectra_subtraction_app.fitter import Fitter, Peak
from spectra_subtraction_app import helpers, plotter

__appname__ = "SpecQP"
__version__ = "0.1"
__authors__ = ["Mikhail Shipilin <mikhail.shipilin@gmail.com>"]
__website__ = "https://github.com/Shipilin/specqp"

__all__ = [
        'datahandler',
        'helpers',
        'fitter',
        'plotter'
        ]
