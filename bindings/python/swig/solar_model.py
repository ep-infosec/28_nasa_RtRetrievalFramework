# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _solar_model.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_solar_model')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_solar_model')
    _solar_model = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_solar_model', [dirname(__file__)])
        except ImportError:
            import _solar_model
            return _solar_model
        try:
            _mod = imp.load_module('_solar_model', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _solar_model = swig_import_helper()
    del swig_import_helper
else:
    import _solar_model
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


class SwigPyIterator(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _solar_model.delete_SwigPyIterator
    def __iter__(self):
        return self
SwigPyIterator.value = new_instancemethod(_solar_model.SwigPyIterator_value, None, SwigPyIterator)
SwigPyIterator.incr = new_instancemethod(_solar_model.SwigPyIterator_incr, None, SwigPyIterator)
SwigPyIterator.decr = new_instancemethod(_solar_model.SwigPyIterator_decr, None, SwigPyIterator)
SwigPyIterator.distance = new_instancemethod(_solar_model.SwigPyIterator_distance, None, SwigPyIterator)
SwigPyIterator.equal = new_instancemethod(_solar_model.SwigPyIterator_equal, None, SwigPyIterator)
SwigPyIterator.copy = new_instancemethod(_solar_model.SwigPyIterator_copy, None, SwigPyIterator)
SwigPyIterator.next = new_instancemethod(_solar_model.SwigPyIterator_next, None, SwigPyIterator)
SwigPyIterator.__next__ = new_instancemethod(_solar_model.SwigPyIterator___next__, None, SwigPyIterator)
SwigPyIterator.previous = new_instancemethod(_solar_model.SwigPyIterator_previous, None, SwigPyIterator)
SwigPyIterator.advance = new_instancemethod(_solar_model.SwigPyIterator_advance, None, SwigPyIterator)
SwigPyIterator.__eq__ = new_instancemethod(_solar_model.SwigPyIterator___eq__, None, SwigPyIterator)
SwigPyIterator.__ne__ = new_instancemethod(_solar_model.SwigPyIterator___ne__, None, SwigPyIterator)
SwigPyIterator.__iadd__ = new_instancemethod(_solar_model.SwigPyIterator___iadd__, None, SwigPyIterator)
SwigPyIterator.__isub__ = new_instancemethod(_solar_model.SwigPyIterator___isub__, None, SwigPyIterator)
SwigPyIterator.__add__ = new_instancemethod(_solar_model.SwigPyIterator___add__, None, SwigPyIterator)
SwigPyIterator.__sub__ = new_instancemethod(_solar_model.SwigPyIterator___sub__, None, SwigPyIterator)
SwigPyIterator_swigregister = _solar_model.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

SHARED_PTR_DISOWN = _solar_model.SHARED_PTR_DISOWN

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

import full_physics_swig.spectrum_effect
import full_physics_swig.generic_object
import full_physics_swig.state_vector
class SolarModel(full_physics_swig.spectrum_effect.SpectrumEffect):
    """

    This applies a solar model to reflectance to model the incoming solar
    irradiance.

    C++ includes: solar_model.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _solar_model.delete_SolarModel

    def apply_solar_model(self, Spec):
        """

        Spectrum SolarModel::apply_solar_model(const Spectrum &Spec) const
        Apply the solar model.

        Parameters:
        -----------

        Spec:  Spectrum without solar model applied. This is per solid angle,
        e.g., sr^-1 (RT code generates "sun-normalized" output)

        Spectrum with solar model applied. 
        """
        return _solar_model.SolarModel_apply_solar_model(self, Spec)


    def solar_spectrum(self, Spec_domain):
        """

        virtual Spectrum FullPhysics::SolarModel::solar_spectrum(const SpectralDomain &Spec_domain) const =0
        Calculate solar spectrum.

        Parameters:
        -----------

        Spec_domain:  Wavenumber/Wavelength reflectance is given

        Solar spectrum. This should have units commensurate with something
        like W / m^2 / cm^-1.  Note that the wavenumber/frequency are in the
        earth rest frame. The solar model may need to work in the solar rest
        frame, bu the conversion to this is internal. The input and output
        from this function should be in the earth rest frame. 
        """
        return _solar_model.SolarModel_solar_spectrum(self, Spec_domain)

SolarModel.apply_solar_model = new_instancemethod(_solar_model.SolarModel_apply_solar_model, None, SolarModel)
SolarModel.solar_spectrum = new_instancemethod(_solar_model.SolarModel_solar_spectrum, None, SolarModel)
SolarModel_swigregister = _solar_model.SolarModel_swigregister
SolarModel_swigregister(SolarModel)

class vector_solar_model(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __iter__(self):
        return self.iterator()

    def __init__(self, *args):
        _solar_model.vector_solar_model_swiginit(self, _solar_model.new_vector_solar_model(*args))
    __swig_destroy__ = _solar_model.delete_vector_solar_model
vector_solar_model.iterator = new_instancemethod(_solar_model.vector_solar_model_iterator, None, vector_solar_model)
vector_solar_model.__nonzero__ = new_instancemethod(_solar_model.vector_solar_model___nonzero__, None, vector_solar_model)
vector_solar_model.__bool__ = new_instancemethod(_solar_model.vector_solar_model___bool__, None, vector_solar_model)
vector_solar_model.__len__ = new_instancemethod(_solar_model.vector_solar_model___len__, None, vector_solar_model)
vector_solar_model.__getslice__ = new_instancemethod(_solar_model.vector_solar_model___getslice__, None, vector_solar_model)
vector_solar_model.__setslice__ = new_instancemethod(_solar_model.vector_solar_model___setslice__, None, vector_solar_model)
vector_solar_model.__delslice__ = new_instancemethod(_solar_model.vector_solar_model___delslice__, None, vector_solar_model)
vector_solar_model.__delitem__ = new_instancemethod(_solar_model.vector_solar_model___delitem__, None, vector_solar_model)
vector_solar_model.__getitem__ = new_instancemethod(_solar_model.vector_solar_model___getitem__, None, vector_solar_model)
vector_solar_model.__setitem__ = new_instancemethod(_solar_model.vector_solar_model___setitem__, None, vector_solar_model)
vector_solar_model.pop = new_instancemethod(_solar_model.vector_solar_model_pop, None, vector_solar_model)
vector_solar_model.append = new_instancemethod(_solar_model.vector_solar_model_append, None, vector_solar_model)
vector_solar_model.empty = new_instancemethod(_solar_model.vector_solar_model_empty, None, vector_solar_model)
vector_solar_model.size = new_instancemethod(_solar_model.vector_solar_model_size, None, vector_solar_model)
vector_solar_model.swap = new_instancemethod(_solar_model.vector_solar_model_swap, None, vector_solar_model)
vector_solar_model.begin = new_instancemethod(_solar_model.vector_solar_model_begin, None, vector_solar_model)
vector_solar_model.end = new_instancemethod(_solar_model.vector_solar_model_end, None, vector_solar_model)
vector_solar_model.rbegin = new_instancemethod(_solar_model.vector_solar_model_rbegin, None, vector_solar_model)
vector_solar_model.rend = new_instancemethod(_solar_model.vector_solar_model_rend, None, vector_solar_model)
vector_solar_model.clear = new_instancemethod(_solar_model.vector_solar_model_clear, None, vector_solar_model)
vector_solar_model.get_allocator = new_instancemethod(_solar_model.vector_solar_model_get_allocator, None, vector_solar_model)
vector_solar_model.pop_back = new_instancemethod(_solar_model.vector_solar_model_pop_back, None, vector_solar_model)
vector_solar_model.erase = new_instancemethod(_solar_model.vector_solar_model_erase, None, vector_solar_model)
vector_solar_model.push_back = new_instancemethod(_solar_model.vector_solar_model_push_back, None, vector_solar_model)
vector_solar_model.front = new_instancemethod(_solar_model.vector_solar_model_front, None, vector_solar_model)
vector_solar_model.back = new_instancemethod(_solar_model.vector_solar_model_back, None, vector_solar_model)
vector_solar_model.assign = new_instancemethod(_solar_model.vector_solar_model_assign, None, vector_solar_model)
vector_solar_model.resize = new_instancemethod(_solar_model.vector_solar_model_resize, None, vector_solar_model)
vector_solar_model.insert = new_instancemethod(_solar_model.vector_solar_model_insert, None, vector_solar_model)
vector_solar_model.reserve = new_instancemethod(_solar_model.vector_solar_model_reserve, None, vector_solar_model)
vector_solar_model.capacity = new_instancemethod(_solar_model.vector_solar_model_capacity, None, vector_solar_model)
vector_solar_model_swigregister = _solar_model.vector_solar_model_swigregister
vector_solar_model_swigregister(vector_solar_model)



