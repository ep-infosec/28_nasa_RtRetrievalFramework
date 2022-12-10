# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _dispersion_fit.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_dispersion_fit')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_dispersion_fit')
    _dispersion_fit = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_dispersion_fit', [dirname(__file__)])
        except ImportError:
            import _dispersion_fit
            return _dispersion_fit
        try:
            _mod = imp.load_module('_dispersion_fit', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _dispersion_fit = swig_import_helper()
    del swig_import_helper
else:
    import _dispersion_fit
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        object.__setattr__(self, name, value)
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_method(set):
    def set_attr(self, name, value):
        if (name == "thisown"):
            return self.this.own(value)
        if hasattr(self, name) or (name == "this"):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add attributes to %s" % self)
    return set_attr


try:
    import weakref
    weakref_proxy = weakref.proxy
except __builtin__.Exception:
    weakref_proxy = lambda x: x


SHARED_PTR_DISOWN = _dispersion_fit.SHARED_PTR_DISOWN

def _new_from_init(cls, version, *args):
    '''For use with pickle, covers common case where we just store the
    arguments needed to create an object. See for example HdfFile'''
    if(cls.pickle_format_version() != version):
      raise RuntimeException("Class is expecting a pickled object with version number %d, but we found %d" % (cls.pickle_format_version(), version))
    inst = cls.__new__(cls)
    inst.__init__(*args)
    return inst

def _new_from_set(cls, version, *args):
    '''For use with pickle, covers common case where we use a set function 
    to assign the value'''
    if(cls.pickle_format_version() != version):
      raise RuntimeException("Class is expecting a pickled object with version number %d, but we found %d" % (cls.pickle_format_version(), version))
    inst = cls.__new__(cls)
    inst.__init__()
    inst.set(*args)
    return inst

import full_physics_swig.generic_object
class DispersionFit(full_physics_swig.generic_object.GenericObject):
    """

    Given a single frame of data, estimate the spectral shift in band 1P.

    This is accomplished by using the strong solar line at 12985.163
    wavenumbers. This is in the a-band continuum and is really the only
    local feature there.

    Note: This routine fits for a global shift, which INCLUDES the
    instrument doppler shift. If this is not desired, the user must
    subtract off the instrument doppler shift.

    Original Author: Chris Odell Converted from IDL

    C++ includes: dispersion_fit.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, Level1b):
        """

        DispersionFit::DispersionFit(const boost::shared_ptr< Level1b > &Level1b)
        Initialize class with data needed to perform fit. 
        """
        _dispersion_fit.DispersionFit_swiginit(self, _dispersion_fit.new_DispersionFit(Level1b))

    def fit(self, disp_initial, aband_solar_line_location, aband_solar_line_width, aband_search_width, aband_ils_offset, offset_scaling):
        """

        blitz::Array< double, 2 > DispersionFit::fit(const blitz::Array< double, 2 > disp_initial, const DoubleWithUnit
        &aband_solar_line_location, const DoubleWithUnit
        &aband_solar_line_width, const DoubleWithUnit &aband_search_width,
        const DoubleWithUnit &aband_ils_offset, const ArrayWithUnit< double, 1
        > &offset_scaling) const

        """
        return _dispersion_fit.DispersionFit_fit(self, disp_initial, aband_solar_line_location, aband_solar_line_width, aband_search_width, aband_ils_offset, offset_scaling)

    __swig_destroy__ = _dispersion_fit.delete_DispersionFit
DispersionFit.fit = new_instancemethod(_dispersion_fit.DispersionFit_fit, None, DispersionFit)
DispersionFit_swigregister = _dispersion_fit.DispersionFit_swigregister
DispersionFit_swigregister(DispersionFit)


