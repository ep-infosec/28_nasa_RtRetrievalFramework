# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _dispersion_fit_output.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_dispersion_fit_output')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_dispersion_fit_output')
    _dispersion_fit_output = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_dispersion_fit_output', [dirname(__file__)])
        except ImportError:
            import _dispersion_fit_output
            return _dispersion_fit_output
        try:
            _mod = imp.load_module('_dispersion_fit_output', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _dispersion_fit_output = swig_import_helper()
    del swig_import_helper
else:
    import _dispersion_fit_output
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


SHARED_PTR_DISOWN = _dispersion_fit_output.SHARED_PTR_DISOWN

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

import full_physics_swig.register_output_base
import full_physics_swig.generic_object
class DispersionFitOutput(full_physics_swig.register_output_base.RegisterOutputBase):
    """

    This registers the portions of the DispersionFit class that should be
    written as output.

    See the discussion in RegisterOutputBase why this isn't just part of
    the DispersionFit class.

    C++ includes: dispersion_fit_output.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def register_output(self, out):
        """

        void DispersionFitOutput::register_output(const boost::shared_ptr< Output > &out) const

        """
        return _dispersion_fit_output.DispersionFitOutput_register_output(self, out)


    def register_output_apriori(self, out):
        """

        void DispersionFitOutput::register_output_apriori(const boost::shared_ptr< Output > &out) const

        """
        return _dispersion_fit_output.DispersionFitOutput_register_output_apriori(self, out)

    __swig_destroy__ = _dispersion_fit_output.delete_DispersionFitOutput
DispersionFitOutput.register_output = new_instancemethod(_dispersion_fit_output.DispersionFitOutput_register_output, None, DispersionFitOutput)
DispersionFitOutput.register_output_apriori = new_instancemethod(_dispersion_fit_output.DispersionFitOutput_register_output_apriori, None, DispersionFitOutput)
DispersionFitOutput_swigregister = _dispersion_fit_output.DispersionFitOutput_swigregister
DispersionFitOutput_swigregister(DispersionFitOutput)



