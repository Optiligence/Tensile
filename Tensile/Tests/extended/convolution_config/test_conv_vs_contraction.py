import logging
from Tensile.SolutionStructs import Convolution
log =logging.getLogger("testlog")

"""
These tests run the convolution-vs-contraction mode always
"""

def test_simple(run_convolution_vs_contraction):
    z={} # problemType definition
    conv = Convolution(z, 'ConvolutionForward',
              config={'TensorAFormat': 'NCHW',
                      })
    log.debug(conv.printUsage(z))
    run_convolution_vs_contraction(conv)


def test_stride1x2(run_convolution_vs_contraction):
    z={} # problemType definition
    conv = Convolution(z, 'ConvolutionForward',
              config={'TensorAFormat': 'NCHW',
                      'Stride': '1x2',
                      })
    log.debug(conv.printUsage(z))
    run_convolution_vs_contraction(conv)

def test_stride2x1(run_convolution_vs_contraction):
    z={} # problemType definition
    conv = Convolution(z, 'ConvolutionForward',
              config={'TensorAFormat': 'NCHW',
                      'Stride': '2x1',
                      })
    log.debug(conv.printUsage(z))
    run_convolution_vs_contraction(conv)

def test_stride2x3(run_convolution_vs_contraction):
    z={} # problemType definition
    conv = Convolution(z, 'ConvolutionForward',
              config={'TensorAFormat': 'NCHW',
                      'Stride': '2x3',
                      })
    log.debug(conv.printUsage(z))
    run_convolution_vs_contraction(conv)

def test_filter1x2(run_convolution_vs_contraction):
    z={} # problemType definition
    conv = Convolution(z, 'ConvolutionForward',
              config={'TensorAFormat': 'NCHW',
                      'Filter': '1x2',
                      })

    log.debug(conv.printUsage(z))
    run_convolution_vs_contraction(conv)


def test_filter2x1(run_convolution_vs_contraction):
    z={} # problemType definition
    conv = Convolution(z, 'ConvolutionForward',
              config={'TensorAFormat': 'NCHW',
                      'Filter': '2x1',
                      })
    log.debug(conv.printUsage(z))
    run_convolution_vs_contraction(conv)

def test_filter2x3(run_convolution_vs_contraction):
    z={} # problemType definition
    conv = Convolution(z, 'ConvolutionForward',
              config={'TensorAFormat': 'NCHW',
                      'Filter': '2x3',
                      })
    log.debug(conv.printUsage(z))
    run_convolution_vs_contraction(conv)

def test_dilation1x2(run_convolution_vs_contraction):
    z={} # problemType definition
    conv = Convolution(z, 'ConvolutionForward',
              config={'TensorAFormat': 'NCHW',
                      'Filter': '2x2',
                      'Dilation': '1x2',
                      })
    log.debug(conv.printUsage(z))
    run_convolution_vs_contraction(conv)

def test_dilation2x1(run_convolution_vs_contraction):
    z={} # problemType definition
    conv = Convolution(z, 'ConvolutionForward',
              config={'TensorAFormat': 'NCHW',
                      'Filter': '2x2',
                      'Dilation': '2x1',
                      })
    log.debug(conv.printUsage(z))
    run_convolution_vs_contraction(conv)

def test_dilation2x3(run_convolution_vs_contraction):
    z={} # problemType definition
    conv = Convolution(z, 'ConvolutionForward',
              config={'TensorAFormat': 'NCHW',
                      'Filter': '2x2',
                      'Dilation': '2x3',
                      })
    log.debug(conv.printUsage(z))
    run_convolution_vs_contraction(conv)

def test_pad1x0(run_convolution_vs_contraction):
    z={} # problemType definition
    conv = Convolution(z, 'ConvolutionForward',
              config={'TensorAFormat': 'NCHW',
                      'Filter': '2x2',
                      'PadStart': '1x0',
                      'PadEnd': '1x0',
                      })
    log.debug(conv.printUsage(z))
    run_convolution_vs_contraction(conv)

def test_pad0x1(run_convolution_vs_contraction):
    z={} # problemType definition
    conv = Convolution(z, 'ConvolutionForward',
              config={'TensorAFormat': 'NCHW',
                      'Filter': '2x2',
                      'PadStart': '0x1',
                      'PadEnd': '0x1',
                      })
    log.debug(conv.printUsage(z))
    run_convolution_vs_contraction(conv)

def test_pad2x3(run_convolution_vs_contraction):
    z={} # problemType definition
    conv = Convolution(z, 'ConvolutionForward',
              config={'TensorAFormat': 'NCHW',
                      'Filter': '2x2',
                      'PadStart': '2x3',
                      'PadEnd': '2x3',
                      })
    log.debug(conv.printUsage(z))
    run_convolution_vs_contraction(conv)


def test_filter_stride_dilation_0(run_convolution_vs_contraction):
    z={} # problemType definition
    conv = Convolution(z, 'ConvolutionForward',
              config={'TensorAFormat': 'NCHW',
                      'TensorBFormat': 'KCYX',
                      'TensorDFormat': 'NCHW',
                      'UnrollOnChannel': 0,
                      'Filter': '2x3',
                      'Stride': '2x3',
                      'Dilation': '2x3',
                      })
    assert(z['NumIndicesC']==4)
    assert(z['IndexAssignmentsA']==[6,5, 0,1, 4,3])
    assert(z['IndexAssignmentsB']==[6,5, 4, 2, 3])
    assert(z['UseInitialStridesAB'])
    log.debug(conv.printUsage(z))
    run_convolution_vs_contraction(conv)

def test_filter_stride_dilation_1(run_convolution_vs_contraction):
    z={} # problemType definition
    conv = Convolution(z, 'ConvolutionForward',
              config={'TensorAFormat': 'NCHW',
                      'Filter': '6x7',
                      'Stride': '2x3',
                      'Dilation': '4x5',
                      'Spatial': '27x51',
                      })
    log.debug(conv.printUsage(z))
    run_convolution_vs_contraction(conv)
