# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _ils_instrument.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_ils_instrument')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_ils_instrument')
    _ils_instrument = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_ils_instrument', [dirname(__file__)])
        except ImportError:
            import _ils_instrument
            return _ils_instrument
        try:
            _mod = imp.load_module('_ils_instrument', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _ils_instrument = swig_import_helper()
    del swig_import_helper
else:
    import _ils_instrument
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


SHARED_PTR_DISOWN = _ils_instrument.SHARED_PTR_DISOWN

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

import full_physics_swig.instrument
import full_physics_swig.generic_object
import full_physics_swig.state_vector
class IlsInstrument(full_physics_swig.instrument.Instrument):
    """

    This is a instrument that uses a Ils object for each spectrometer to
    model the instrument.

    C++ includes: ils_instrument.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def notify_update(self, *args):
        """

        virtual void FullPhysics::IlsInstrument::notify_update(const InstrumentCorrection &C)

        """
        return _ils_instrument.IlsInstrument_notify_update(self, *args)


    def ils(self, Spec_index):
        """

        boost::shared_ptr<Ils> FullPhysics::IlsInstrument::ils(int Spec_index) const
        Underlying Ils. 
        """
        return _ils_instrument.IlsInstrument_ils(self, Spec_index)


    def instrument_correction(self, Spec_index):
        """

        const std::vector<boost::shared_ptr<InstrumentCorrection> >& FullPhysics::IlsInstrument::instrument_correction(int Spec_index) const
        Underlying InstrumentCorrection. 
        """
        return _ils_instrument.IlsInstrument_instrument_correction(self, Spec_index)

    __swig_destroy__ = _ils_instrument.delete_IlsInstrument
IlsInstrument.notify_update = new_instancemethod(_ils_instrument.IlsInstrument_notify_update, None, IlsInstrument)
IlsInstrument.ils = new_instancemethod(_ils_instrument.IlsInstrument_ils, None, IlsInstrument)
IlsInstrument.instrument_correction = new_instancemethod(_ils_instrument.IlsInstrument_instrument_correction, None, IlsInstrument)
IlsInstrument_swigregister = _ils_instrument.IlsInstrument_swigregister
IlsInstrument_swigregister(IlsInstrument)



