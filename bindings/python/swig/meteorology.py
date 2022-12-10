# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _meteorology.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_meteorology')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_meteorology')
    _meteorology = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_meteorology', [dirname(__file__)])
        except ImportError:
            import _meteorology
            return _meteorology
        try:
            _mod = imp.load_module('_meteorology', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _meteorology = swig_import_helper()
    del swig_import_helper
else:
    import _meteorology
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


SHARED_PTR_DISOWN = _meteorology.SHARED_PTR_DISOWN

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
class Meteorology(full_physics_swig.generic_object.GenericObject):
    """

    Defines the interface for supplying meteorological data.

    Routines are provided to interpolate the values to a different
    pressure levels grid for values with a profile.

    C++ includes: meteorology.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __swig_destroy__ = _meteorology.delete_Meteorology

    def _v_pressure_levels(self):
        """

        virtual blitz::Array<double, 1> FullPhysics::Meteorology::pressure_levels() const =0
        Pressure levels in Pascals used for provided meteorological data. 
        """
        return _meteorology.Meteorology__v_pressure_levels(self)


    @property
    def pressure_levels(self):
        return self._v_pressure_levels()


    @property
    def specific_humidity(self):
        return self._v_specific_humidity()


    def _v_specific_humidity(self, *args):
        """

        virtual blitz::Array<double, 1> FullPhysics::Meteorology::specific_humidity(const blitz::Array< double, 1 > &Pressure_level) const
        Specific humidity interpolated to the requested pressure levels. 
        """
        return _meteorology.Meteorology__v_specific_humidity(self, *args)


    def vmr(self, *args):
        """

        virtual blitz::Array<double, 1> FullPhysics::Meteorology::vmr(const std::string &Species, const blitz::Array< double, 1 >
        &Pressure_level) const
        Volume mixing ratio for a particular species interpolated to the
        requested pressure levels. 
        """
        return _meteorology.Meteorology_vmr(self, *args)


    @property
    def temperature(self):
        return self._v_temperature()


    def _v_temperature(self, *args):
        """

        virtual blitz::Array<double, 1> FullPhysics::Meteorology::temperature(const blitz::Array< double, 1 > &Pressure_level) const
        Temperature profile in Kelvins interpolated to the requested pressure
        levels. 
        """
        return _meteorology.Meteorology__v_temperature(self, *args)


    def _v_surface_pressure(self):
        """

        virtual double FullPhysics::Meteorology::surface_pressure() const =0
        Surface pressure in Pascals. 
        """
        return _meteorology.Meteorology__v_surface_pressure(self)


    @property
    def surface_pressure(self):
        return self._v_surface_pressure()


    def _v_windspeed(self):
        """

        double Meteorology::windspeed() const
        Windspeed magnitude in m/s for the surface. 
        """
        return _meteorology.Meteorology__v_windspeed(self)


    @property
    def windspeed(self):
        return self._v_windspeed()


    def _v_windspeed_u(self):
        """

        virtual double FullPhysics::Meteorology::windspeed_u() const =0
        The U component windspeed in m/s. 
        """
        return _meteorology.Meteorology__v_windspeed_u(self)


    @property
    def windspeed_u(self):
        return self._v_windspeed_u()


    def _v_windspeed_v(self):
        """

        virtual double FullPhysics::Meteorology::windspeed_v() const =0
        The V component windspeed in m/s. 
        """
        return _meteorology.Meteorology__v_windspeed_v(self)


    @property
    def windspeed_v(self):
        return self._v_windspeed_v()

Meteorology.__str__ = new_instancemethod(_meteorology.Meteorology___str__, None, Meteorology)
Meteorology._v_pressure_levels = new_instancemethod(_meteorology.Meteorology__v_pressure_levels, None, Meteorology)
Meteorology._v_specific_humidity = new_instancemethod(_meteorology.Meteorology__v_specific_humidity, None, Meteorology)
Meteorology.vmr = new_instancemethod(_meteorology.Meteorology_vmr, None, Meteorology)
Meteorology._v_temperature = new_instancemethod(_meteorology.Meteorology__v_temperature, None, Meteorology)
Meteorology._v_surface_pressure = new_instancemethod(_meteorology.Meteorology__v_surface_pressure, None, Meteorology)
Meteorology._v_windspeed = new_instancemethod(_meteorology.Meteorology__v_windspeed, None, Meteorology)
Meteorology._v_windspeed_u = new_instancemethod(_meteorology.Meteorology__v_windspeed_u, None, Meteorology)
Meteorology._v_windspeed_v = new_instancemethod(_meteorology.Meteorology__v_windspeed_v, None, Meteorology)
Meteorology_swigregister = _meteorology.Meteorology_swigregister
Meteorology_swigregister(Meteorology)


