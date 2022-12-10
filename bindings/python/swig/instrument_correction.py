# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _instrument_correction.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_instrument_correction')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_instrument_correction')
    _instrument_correction = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_instrument_correction', [dirname(__file__)])
        except ImportError:
            import _instrument_correction
            return _instrument_correction
        try:
            _mod = imp.load_module('_instrument_correction', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _instrument_correction = swig_import_helper()
    del swig_import_helper
else:
    import _instrument_correction
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


SHARED_PTR_DISOWN = _instrument_correction.SHARED_PTR_DISOWN

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
class ObservableInstrumentCorrection(full_physics_swig.generic_object.GenericObject):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _instrument_correction.delete_ObservableInstrumentCorrection
ObservableInstrumentCorrection.add_observer_and_keep_reference = new_instancemethod(_instrument_correction.ObservableInstrumentCorrection_add_observer_and_keep_reference, None, ObservableInstrumentCorrection)
ObservableInstrumentCorrection.add_observer = new_instancemethod(_instrument_correction.ObservableInstrumentCorrection_add_observer, None, ObservableInstrumentCorrection)
ObservableInstrumentCorrection.remove_observer = new_instancemethod(_instrument_correction.ObservableInstrumentCorrection_remove_observer, None, ObservableInstrumentCorrection)
ObservableInstrumentCorrection_swigregister = _instrument_correction.ObservableInstrumentCorrection_swigregister
ObservableInstrumentCorrection_swigregister(ObservableInstrumentCorrection)

class ObserverInstrumentCorrection(full_physics_swig.generic_object.GenericObject):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self):
        _instrument_correction.ObserverInstrumentCorrection_swiginit(self, _instrument_correction.new_ObserverInstrumentCorrection())
    __swig_destroy__ = _instrument_correction.delete_ObserverInstrumentCorrection
ObserverInstrumentCorrection.notify_update = new_instancemethod(_instrument_correction.ObserverInstrumentCorrection_notify_update, None, ObserverInstrumentCorrection)
ObserverInstrumentCorrection.notify_add = new_instancemethod(_instrument_correction.ObserverInstrumentCorrection_notify_add, None, ObserverInstrumentCorrection)
ObserverInstrumentCorrection.notify_remove = new_instancemethod(_instrument_correction.ObserverInstrumentCorrection_notify_remove, None, ObserverInstrumentCorrection)
ObserverInstrumentCorrection_swigregister = _instrument_correction.ObserverInstrumentCorrection_swigregister
ObserverInstrumentCorrection_swigregister(ObserverInstrumentCorrection)

class InstrumentCorrection(full_physics_swig.state_vector.StateVectorObserver, ObservableInstrumentCorrection):
    """

    This class models an Instrument correction.

    This is used by IlsConvolution, and it applies zero or more
    corrections that allow the radiance results to be modified. Examples
    are a zero level offset correction, and a continuum correction.

    C++ includes: instrument_correction.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _instrument_correction.delete_InstrumentCorrection

    def apply_correction(self, Pixel_grid, Pixel_list, Radiance):
        """

        virtual void FullPhysics::InstrumentCorrection::apply_correction(const SpectralDomain &Pixel_grid, const std::vector< int >
        &Pixel_list, SpectralRange &Radiance) const =0
        Apply correction to radiance values, in place.

        If Radiance includes a Jacobian, then we include the Jacobian
        calculation. Otherwise we don't include the Jacobian in the
        calculation.

        Parameters:
        -----------

        Pixel_grid:  - The grid point of each pixel. We only use a subset of
        these points, but the full list is passed in for use by the class.

        Pixel_list:  - List of pixels that actually appear in Radiance, in the
        order that they appear.

        Radiance:  - Radiance values, that will be corrected in place. 
        """
        return _instrument_correction.InstrumentCorrection_apply_correction(self, Pixel_grid, Pixel_list, Radiance)


    def clone(self):
        """

        virtual boost::shared_ptr<InstrumentCorrection> FullPhysics::InstrumentCorrection::clone() const =0
        Clone an InstrumentCorrection object.

        Note that the cloned version will not be attached to and StateVector
        or Observer<InstrumentCorrection>, although you can of course attach
        them after receiving the cloned object.

        Because this isn't attached to the StateVector, one use of the clone
        operator is to create a "frozen" InstrumentCorrection object. 
        """
        return _instrument_correction.InstrumentCorrection_clone(self)

InstrumentCorrection.__str__ = new_instancemethod(_instrument_correction.InstrumentCorrection___str__, None, InstrumentCorrection)
InstrumentCorrection.apply_correction = new_instancemethod(_instrument_correction.InstrumentCorrection_apply_correction, None, InstrumentCorrection)
InstrumentCorrection.clone = new_instancemethod(_instrument_correction.InstrumentCorrection_clone, None, InstrumentCorrection)
InstrumentCorrection_swigregister = _instrument_correction.InstrumentCorrection_swigregister
InstrumentCorrection_swigregister(InstrumentCorrection)

class SubStateVectorArrayInstrumentCorrection(InstrumentCorrection, full_physics_swig.state_vector.SubStateVectorObserver):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _instrument_correction.delete_SubStateVectorArrayInstrumentCorrection

    @property
    def coefficient(self):
        return self._v_coefficient()


    @property
    def used_flag_value(self):
        return self._v_used_flag_value()


    @property
    def statevector_covariance(self):
        return self._v_statevector_covariance()


    @property
    def pressure(self):
        return self._v_pressure()

SubStateVectorArrayInstrumentCorrection.init = new_instancemethod(_instrument_correction.SubStateVectorArrayInstrumentCorrection_init, None, SubStateVectorArrayInstrumentCorrection)
SubStateVectorArrayInstrumentCorrection.state_vector_name_i = new_instancemethod(_instrument_correction.SubStateVectorArrayInstrumentCorrection_state_vector_name_i, None, SubStateVectorArrayInstrumentCorrection)
SubStateVectorArrayInstrumentCorrection.update_sub_state_hook = new_instancemethod(_instrument_correction.SubStateVectorArrayInstrumentCorrection_update_sub_state_hook, None, SubStateVectorArrayInstrumentCorrection)
SubStateVectorArrayInstrumentCorrection._v_coefficient = new_instancemethod(_instrument_correction.SubStateVectorArrayInstrumentCorrection__v_coefficient, None, SubStateVectorArrayInstrumentCorrection)
SubStateVectorArrayInstrumentCorrection._v_used_flag_value = new_instancemethod(_instrument_correction.SubStateVectorArrayInstrumentCorrection__v_used_flag_value, None, SubStateVectorArrayInstrumentCorrection)
SubStateVectorArrayInstrumentCorrection._v_statevector_covariance = new_instancemethod(_instrument_correction.SubStateVectorArrayInstrumentCorrection__v_statevector_covariance, None, SubStateVectorArrayInstrumentCorrection)
SubStateVectorArrayInstrumentCorrection._v_pressure = new_instancemethod(_instrument_correction.SubStateVectorArrayInstrumentCorrection__v_pressure, None, SubStateVectorArrayInstrumentCorrection)
SubStateVectorArrayInstrumentCorrection_swigregister = _instrument_correction.SubStateVectorArrayInstrumentCorrection_swigregister
SubStateVectorArrayInstrumentCorrection_swigregister(SubStateVectorArrayInstrumentCorrection)


