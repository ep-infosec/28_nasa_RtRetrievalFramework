# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _pressure.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_pressure')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_pressure')
    _pressure = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_pressure', [dirname(__file__)])
        except ImportError:
            import _pressure
            return _pressure
        try:
            _mod = imp.load_module('_pressure', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _pressure = swig_import_helper()
    del swig_import_helper
else:
    import _pressure
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


SHARED_PTR_DISOWN = _pressure.SHARED_PTR_DISOWN

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

import full_physics_swig.state_vector
import full_physics_swig.generic_object
class ObservablePressure(full_physics_swig.generic_object.GenericObject):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _pressure.delete_ObservablePressure
ObservablePressure.add_observer_and_keep_reference = new_instancemethod(_pressure.ObservablePressure_add_observer_and_keep_reference, None, ObservablePressure)
ObservablePressure.add_observer = new_instancemethod(_pressure.ObservablePressure_add_observer, None, ObservablePressure)
ObservablePressure.remove_observer = new_instancemethod(_pressure.ObservablePressure_remove_observer, None, ObservablePressure)
ObservablePressure_swigregister = _pressure.ObservablePressure_swigregister
ObservablePressure_swigregister(ObservablePressure)

class ObserverPressure(full_physics_swig.generic_object.GenericObject):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self):
        _pressure.ObserverPressure_swiginit(self, _pressure.new_ObserverPressure())
    __swig_destroy__ = _pressure.delete_ObserverPressure
ObserverPressure.notify_update = new_instancemethod(_pressure.ObserverPressure_notify_update, None, ObserverPressure)
ObserverPressure.notify_add = new_instancemethod(_pressure.ObserverPressure_notify_add, None, ObserverPressure)
ObserverPressure.notify_remove = new_instancemethod(_pressure.ObserverPressure_notify_remove, None, ObserverPressure)
ObserverPressure_swigregister = _pressure.ObserverPressure_swigregister
ObserverPressure_swigregister(ObserverPressure)

class Pressure(full_physics_swig.state_vector.StateVectorObserver, ObservablePressure):
    """

    This class maintains the pressure portion of the state.

    Note that in a retrieval, there are typically two different pressure
    levels of interest. On is the pressure levels where various initial
    parameters are defined, e.g. Temperature read from an ECMWF file at
    specific pressure levels. The second set is the current pressure
    levels that define the layers used in the Radiative Transfer
    calculation. The first set is fixed constant level, it is whatever was
    used when we initial read the input data. The second will potentially
    vary as we do a retrieval.

    This class captures the second, potentially varying set of pressure.

    Other classes typically depend on the pressure levels, e.g., Altitude.
    As a convenience to these classes, the Pressure class can notify them
    when it is changed. These classes can register themselves as Observers
    of the Pressure object if desired.

    When implementing a new class, you almost always will want to derive
    from PressureImpBase rather than from this class. See that class for a
    description.

    C++ includes: pressure.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    __swig_destroy__ = _pressure.delete_Pressure

    def add_observer(self, Obs):
        """

        virtual void FullPhysics::Pressure::add_observer(Observer< Pressure > &Obs)

        """
        return _pressure.Pressure_add_observer(self, Obs)


    def remove_observer(self, Obs):
        """

        virtual void FullPhysics::Pressure::remove_observer(Observer< Pressure > &Obs)

        """
        return _pressure.Pressure_remove_observer(self, Obs)


    def _v_surface_pressure(self):
        """

        AutoDerivativeWithUnit< double > Pressure::surface_pressure() const
        Return surface pressure, which is just the pressure at the bottom
        level of pressure_grid.

        This is in Pascals. 
        """
        return _pressure.Pressure__v_surface_pressure(self)


    @property
    def surface_pressure(self):
        return self._v_surface_pressure()


    def _v_surface_pressure_value(self):
        """

        double FullPhysics::Pressure::surface_pressure_value() const
        Return the current surface pressure value, without the gradient.

        This is in Pascals. 
        """
        return _pressure.Pressure__v_surface_pressure_value(self)


    @property
    def surface_pressure_value(self):
        return self._v_surface_pressure_value()


    def _v_pressure_grid(self):
        """

        virtual ArrayAdWithUnit<double, 1> FullPhysics::Pressure::pressure_grid() const =0
        This returns the pressure grid to use for layer retrieval, along with
        the gradient of each of the pressure grid values with the state
        vector. 
        """
        return _pressure.Pressure__v_pressure_grid(self)


    @property
    def pressure_grid(self):
        return self._v_pressure_grid()


    def _v_number_layer(self):
        """

        int FullPhysics::Pressure::number_layer() const
        This is the number of layers.

        This is the same as pressure_grid.rows() - 1. 
        """
        return _pressure.Pressure__v_number_layer(self)


    @property
    def number_layer(self):
        return self._v_number_layer()


    def _v_number_level(self):
        """

        int FullPhysics::Pressure::number_level() const
        This is the number of levels.

        This is the same as pressure_grid.rows() - 1. 
        """
        return _pressure.Pressure__v_number_level(self)


    @property
    def number_level(self):
        return self._v_number_level()


    def _v_max_number_level(self):
        """

        virtual int FullPhysics::Pressure::max_number_level() const
        The maximum number of levels that we can have.

        The default is just number_level() (i.e., we don't change the number
        of levels from one iteration to the next). 
        """
        return _pressure.Pressure__v_max_number_level(self)


    @property
    def max_number_level(self):
        return self._v_max_number_level()


    def clone(self):
        """

        virtual boost::shared_ptr<Pressure> FullPhysics::Pressure::clone() const =0
        Clone a Pressure object.

        Note that the cloned version will not be attached to a StateVector or
        Observer<Pressure>, although you can of course attach them after
        receiving the cloned object.

        Because this isn't attached to the StateVector, one use of the clone
        operator is to create a "frozen" Pressure object. 
        """
        return _pressure.Pressure_clone(self)


    def __init__(self):
        if self.__class__ == Pressure:
            _self = None
        else:
            _self = self
        _pressure.Pressure_swiginit(self, _pressure.new_Pressure(_self, ))
    def __disown__(self):
        self.this.disown()
        _pressure.disown_Pressure(self)
        return weakref_proxy(self)
Pressure.add_observer = new_instancemethod(_pressure.Pressure_add_observer, None, Pressure)
Pressure.remove_observer = new_instancemethod(_pressure.Pressure_remove_observer, None, Pressure)
Pressure._v_surface_pressure = new_instancemethod(_pressure.Pressure__v_surface_pressure, None, Pressure)
Pressure._v_surface_pressure_value = new_instancemethod(_pressure.Pressure__v_surface_pressure_value, None, Pressure)
Pressure._v_pressure_grid = new_instancemethod(_pressure.Pressure__v_pressure_grid, None, Pressure)
Pressure._v_number_layer = new_instancemethod(_pressure.Pressure__v_number_layer, None, Pressure)
Pressure._v_number_level = new_instancemethod(_pressure.Pressure__v_number_level, None, Pressure)
Pressure._v_max_number_level = new_instancemethod(_pressure.Pressure__v_max_number_level, None, Pressure)
Pressure.clone = new_instancemethod(_pressure.Pressure_clone, None, Pressure)
Pressure.__str__ = new_instancemethod(_pressure.Pressure___str__, None, Pressure)
Pressure_swigregister = _pressure.Pressure_swigregister
Pressure_swigregister(Pressure)



