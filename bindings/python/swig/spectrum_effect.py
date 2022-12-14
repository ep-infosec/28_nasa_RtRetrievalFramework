# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _spectrum_effect.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_spectrum_effect')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_spectrum_effect')
    _spectrum_effect = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_spectrum_effect', [dirname(__file__)])
        except ImportError:
            import _spectrum_effect
            return _spectrum_effect
        try:
            _mod = imp.load_module('_spectrum_effect', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _spectrum_effect = swig_import_helper()
    del swig_import_helper
else:
    import _spectrum_effect
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
    __swig_destroy__ = _spectrum_effect.delete_SwigPyIterator
    def __iter__(self):
        return self
SwigPyIterator.value = new_instancemethod(_spectrum_effect.SwigPyIterator_value, None, SwigPyIterator)
SwigPyIterator.incr = new_instancemethod(_spectrum_effect.SwigPyIterator_incr, None, SwigPyIterator)
SwigPyIterator.decr = new_instancemethod(_spectrum_effect.SwigPyIterator_decr, None, SwigPyIterator)
SwigPyIterator.distance = new_instancemethod(_spectrum_effect.SwigPyIterator_distance, None, SwigPyIterator)
SwigPyIterator.equal = new_instancemethod(_spectrum_effect.SwigPyIterator_equal, None, SwigPyIterator)
SwigPyIterator.copy = new_instancemethod(_spectrum_effect.SwigPyIterator_copy, None, SwigPyIterator)
SwigPyIterator.next = new_instancemethod(_spectrum_effect.SwigPyIterator_next, None, SwigPyIterator)
SwigPyIterator.__next__ = new_instancemethod(_spectrum_effect.SwigPyIterator___next__, None, SwigPyIterator)
SwigPyIterator.previous = new_instancemethod(_spectrum_effect.SwigPyIterator_previous, None, SwigPyIterator)
SwigPyIterator.advance = new_instancemethod(_spectrum_effect.SwigPyIterator_advance, None, SwigPyIterator)
SwigPyIterator.__eq__ = new_instancemethod(_spectrum_effect.SwigPyIterator___eq__, None, SwigPyIterator)
SwigPyIterator.__ne__ = new_instancemethod(_spectrum_effect.SwigPyIterator___ne__, None, SwigPyIterator)
SwigPyIterator.__iadd__ = new_instancemethod(_spectrum_effect.SwigPyIterator___iadd__, None, SwigPyIterator)
SwigPyIterator.__isub__ = new_instancemethod(_spectrum_effect.SwigPyIterator___isub__, None, SwigPyIterator)
SwigPyIterator.__add__ = new_instancemethod(_spectrum_effect.SwigPyIterator___add__, None, SwigPyIterator)
SwigPyIterator.__sub__ = new_instancemethod(_spectrum_effect.SwigPyIterator___sub__, None, SwigPyIterator)
SwigPyIterator_swigregister = _spectrum_effect.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

SHARED_PTR_DISOWN = _spectrum_effect.SHARED_PTR_DISOWN

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
import full_physics_swig.state_vector
class ObservableSpectrumEffect(full_physics_swig.generic_object.GenericObject):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _spectrum_effect.delete_ObservableSpectrumEffect
ObservableSpectrumEffect.add_observer_and_keep_reference = new_instancemethod(_spectrum_effect.ObservableSpectrumEffect_add_observer_and_keep_reference, None, ObservableSpectrumEffect)
ObservableSpectrumEffect.add_observer = new_instancemethod(_spectrum_effect.ObservableSpectrumEffect_add_observer, None, ObservableSpectrumEffect)
ObservableSpectrumEffect.remove_observer = new_instancemethod(_spectrum_effect.ObservableSpectrumEffect_remove_observer, None, ObservableSpectrumEffect)
ObservableSpectrumEffect_swigregister = _spectrum_effect.ObservableSpectrumEffect_swigregister
ObservableSpectrumEffect_swigregister(ObservableSpectrumEffect)

class ObserverSpectrumEffect(full_physics_swig.generic_object.GenericObject):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self):
        _spectrum_effect.ObserverSpectrumEffect_swiginit(self, _spectrum_effect.new_ObserverSpectrumEffect())
    __swig_destroy__ = _spectrum_effect.delete_ObserverSpectrumEffect
ObserverSpectrumEffect.notify_update = new_instancemethod(_spectrum_effect.ObserverSpectrumEffect_notify_update, None, ObserverSpectrumEffect)
ObserverSpectrumEffect.notify_add = new_instancemethod(_spectrum_effect.ObserverSpectrumEffect_notify_add, None, ObserverSpectrumEffect)
ObserverSpectrumEffect.notify_remove = new_instancemethod(_spectrum_effect.ObserverSpectrumEffect_notify_remove, None, ObserverSpectrumEffect)
ObserverSpectrumEffect_swigregister = _spectrum_effect.ObserverSpectrumEffect_swigregister
ObserverSpectrumEffect_swigregister(ObserverSpectrumEffect)

class SpectrumEffect(full_physics_swig.state_vector.StateVectorObserver, ObservableSpectrumEffect):
    """

    This class models models any effects that need to be applied to high
    resolution spectra after the radiative transfer model has finished its
    work.

    C++ includes: spectrum_effect.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _spectrum_effect.delete_SpectrumEffect

    def apply_effect(self, Spec, Forward_model_grid):
        """

        virtual void FullPhysics::SpectrumEffect::apply_effect(Spectrum &Spec, const ForwardModelSpectralGrid &Forward_model_grid)
        const =0
        Apply correction to spectrum in place.

        We pass in the forward model grids used. A class can use this to
        optimize its calculation, see for example FluorescenceEffect. 
        """
        return _spectrum_effect.SpectrumEffect_apply_effect(self, Spec, Forward_model_grid)


    def clone(self):
        """

        virtual boost::shared_ptr<SpectrumEffect> FullPhysics::SpectrumEffect::clone() const =0
        Clone a SpectrumEffect object.

        Note that the cloned version will not be attached to and StateVector
        or Observer<SpectrumEffect>, although you can of course attach them
        after receiving the cloned object.

        Because this isn't attached to the StateVector, one use of the clone
        operator is to create a "frozen" SpectrumEffect object. 
        """
        return _spectrum_effect.SpectrumEffect_clone(self)


    def _v_name(self):
        """

        virtual std::string FullPhysics::SpectrumEffect::name() const =0
        Name of spectrum effect, for use when outputting effects of effect. 
        """
        return _spectrum_effect.SpectrumEffect__v_name(self)


    @property
    def name(self):
        return self._v_name()

SpectrumEffect.__str__ = new_instancemethod(_spectrum_effect.SpectrumEffect___str__, None, SpectrumEffect)
SpectrumEffect.apply_effect = new_instancemethod(_spectrum_effect.SpectrumEffect_apply_effect, None, SpectrumEffect)
SpectrumEffect.clone = new_instancemethod(_spectrum_effect.SpectrumEffect_clone, None, SpectrumEffect)
SpectrumEffect._v_name = new_instancemethod(_spectrum_effect.SpectrumEffect__v_name, None, SpectrumEffect)
SpectrumEffect_swigregister = _spectrum_effect.SpectrumEffect_swigregister
SpectrumEffect_swigregister(SpectrumEffect)

class SubStateVectorArraySpectrumEffect(SpectrumEffect, full_physics_swig.state_vector.SubStateVectorObserver):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _spectrum_effect.delete_SubStateVectorArraySpectrumEffect

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

SubStateVectorArraySpectrumEffect.init = new_instancemethod(_spectrum_effect.SubStateVectorArraySpectrumEffect_init, None, SubStateVectorArraySpectrumEffect)
SubStateVectorArraySpectrumEffect.state_vector_name_i = new_instancemethod(_spectrum_effect.SubStateVectorArraySpectrumEffect_state_vector_name_i, None, SubStateVectorArraySpectrumEffect)
SubStateVectorArraySpectrumEffect.update_sub_state_hook = new_instancemethod(_spectrum_effect.SubStateVectorArraySpectrumEffect_update_sub_state_hook, None, SubStateVectorArraySpectrumEffect)
SubStateVectorArraySpectrumEffect._v_coefficient = new_instancemethod(_spectrum_effect.SubStateVectorArraySpectrumEffect__v_coefficient, None, SubStateVectorArraySpectrumEffect)
SubStateVectorArraySpectrumEffect._v_used_flag_value = new_instancemethod(_spectrum_effect.SubStateVectorArraySpectrumEffect__v_used_flag_value, None, SubStateVectorArraySpectrumEffect)
SubStateVectorArraySpectrumEffect._v_statevector_covariance = new_instancemethod(_spectrum_effect.SubStateVectorArraySpectrumEffect__v_statevector_covariance, None, SubStateVectorArraySpectrumEffect)
SubStateVectorArraySpectrumEffect._v_pressure = new_instancemethod(_spectrum_effect.SubStateVectorArraySpectrumEffect__v_pressure, None, SubStateVectorArraySpectrumEffect)
SubStateVectorArraySpectrumEffect_swigregister = _spectrum_effect.SubStateVectorArraySpectrumEffect_swigregister
SubStateVectorArraySpectrumEffect_swigregister(SubStateVectorArraySpectrumEffect)

class vector_spectrum_effect(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __iter__(self):
        return self.iterator()

    def __init__(self, *args):
        _spectrum_effect.vector_spectrum_effect_swiginit(self, _spectrum_effect.new_vector_spectrum_effect(*args))
    __swig_destroy__ = _spectrum_effect.delete_vector_spectrum_effect
vector_spectrum_effect.iterator = new_instancemethod(_spectrum_effect.vector_spectrum_effect_iterator, None, vector_spectrum_effect)
vector_spectrum_effect.__nonzero__ = new_instancemethod(_spectrum_effect.vector_spectrum_effect___nonzero__, None, vector_spectrum_effect)
vector_spectrum_effect.__bool__ = new_instancemethod(_spectrum_effect.vector_spectrum_effect___bool__, None, vector_spectrum_effect)
vector_spectrum_effect.__len__ = new_instancemethod(_spectrum_effect.vector_spectrum_effect___len__, None, vector_spectrum_effect)
vector_spectrum_effect.__getslice__ = new_instancemethod(_spectrum_effect.vector_spectrum_effect___getslice__, None, vector_spectrum_effect)
vector_spectrum_effect.__setslice__ = new_instancemethod(_spectrum_effect.vector_spectrum_effect___setslice__, None, vector_spectrum_effect)
vector_spectrum_effect.__delslice__ = new_instancemethod(_spectrum_effect.vector_spectrum_effect___delslice__, None, vector_spectrum_effect)
vector_spectrum_effect.__delitem__ = new_instancemethod(_spectrum_effect.vector_spectrum_effect___delitem__, None, vector_spectrum_effect)
vector_spectrum_effect.__getitem__ = new_instancemethod(_spectrum_effect.vector_spectrum_effect___getitem__, None, vector_spectrum_effect)
vector_spectrum_effect.__setitem__ = new_instancemethod(_spectrum_effect.vector_spectrum_effect___setitem__, None, vector_spectrum_effect)
vector_spectrum_effect.pop = new_instancemethod(_spectrum_effect.vector_spectrum_effect_pop, None, vector_spectrum_effect)
vector_spectrum_effect.append = new_instancemethod(_spectrum_effect.vector_spectrum_effect_append, None, vector_spectrum_effect)
vector_spectrum_effect.empty = new_instancemethod(_spectrum_effect.vector_spectrum_effect_empty, None, vector_spectrum_effect)
vector_spectrum_effect.size = new_instancemethod(_spectrum_effect.vector_spectrum_effect_size, None, vector_spectrum_effect)
vector_spectrum_effect.swap = new_instancemethod(_spectrum_effect.vector_spectrum_effect_swap, None, vector_spectrum_effect)
vector_spectrum_effect.begin = new_instancemethod(_spectrum_effect.vector_spectrum_effect_begin, None, vector_spectrum_effect)
vector_spectrum_effect.end = new_instancemethod(_spectrum_effect.vector_spectrum_effect_end, None, vector_spectrum_effect)
vector_spectrum_effect.rbegin = new_instancemethod(_spectrum_effect.vector_spectrum_effect_rbegin, None, vector_spectrum_effect)
vector_spectrum_effect.rend = new_instancemethod(_spectrum_effect.vector_spectrum_effect_rend, None, vector_spectrum_effect)
vector_spectrum_effect.clear = new_instancemethod(_spectrum_effect.vector_spectrum_effect_clear, None, vector_spectrum_effect)
vector_spectrum_effect.get_allocator = new_instancemethod(_spectrum_effect.vector_spectrum_effect_get_allocator, None, vector_spectrum_effect)
vector_spectrum_effect.pop_back = new_instancemethod(_spectrum_effect.vector_spectrum_effect_pop_back, None, vector_spectrum_effect)
vector_spectrum_effect.erase = new_instancemethod(_spectrum_effect.vector_spectrum_effect_erase, None, vector_spectrum_effect)
vector_spectrum_effect.push_back = new_instancemethod(_spectrum_effect.vector_spectrum_effect_push_back, None, vector_spectrum_effect)
vector_spectrum_effect.front = new_instancemethod(_spectrum_effect.vector_spectrum_effect_front, None, vector_spectrum_effect)
vector_spectrum_effect.back = new_instancemethod(_spectrum_effect.vector_spectrum_effect_back, None, vector_spectrum_effect)
vector_spectrum_effect.assign = new_instancemethod(_spectrum_effect.vector_spectrum_effect_assign, None, vector_spectrum_effect)
vector_spectrum_effect.resize = new_instancemethod(_spectrum_effect.vector_spectrum_effect_resize, None, vector_spectrum_effect)
vector_spectrum_effect.insert = new_instancemethod(_spectrum_effect.vector_spectrum_effect_insert, None, vector_spectrum_effect)
vector_spectrum_effect.reserve = new_instancemethod(_spectrum_effect.vector_spectrum_effect_reserve, None, vector_spectrum_effect)
vector_spectrum_effect.capacity = new_instancemethod(_spectrum_effect.vector_spectrum_effect_capacity, None, vector_spectrum_effect)
vector_spectrum_effect_swigregister = _spectrum_effect.vector_spectrum_effect_swigregister
vector_spectrum_effect_swigregister(vector_spectrum_effect)

class vector_vector_spectrum_effect(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __iter__(self):
        return self.iterator()

    def __init__(self, *args):
        _spectrum_effect.vector_vector_spectrum_effect_swiginit(self, _spectrum_effect.new_vector_vector_spectrum_effect(*args))
    __swig_destroy__ = _spectrum_effect.delete_vector_vector_spectrum_effect
vector_vector_spectrum_effect.iterator = new_instancemethod(_spectrum_effect.vector_vector_spectrum_effect_iterator, None, vector_vector_spectrum_effect)
vector_vector_spectrum_effect.__nonzero__ = new_instancemethod(_spectrum_effect.vector_vector_spectrum_effect___nonzero__, None, vector_vector_spectrum_effect)
vector_vector_spectrum_effect.__bool__ = new_instancemethod(_spectrum_effect.vector_vector_spectrum_effect___bool__, None, vector_vector_spectrum_effect)
vector_vector_spectrum_effect.__len__ = new_instancemethod(_spectrum_effect.vector_vector_spectrum_effect___len__, None, vector_vector_spectrum_effect)
vector_vector_spectrum_effect.__getslice__ = new_instancemethod(_spectrum_effect.vector_vector_spectrum_effect___getslice__, None, vector_vector_spectrum_effect)
vector_vector_spectrum_effect.__setslice__ = new_instancemethod(_spectrum_effect.vector_vector_spectrum_effect___setslice__, None, vector_vector_spectrum_effect)
vector_vector_spectrum_effect.__delslice__ = new_instancemethod(_spectrum_effect.vector_vector_spectrum_effect___delslice__, None, vector_vector_spectrum_effect)
vector_vector_spectrum_effect.__delitem__ = new_instancemethod(_spectrum_effect.vector_vector_spectrum_effect___delitem__, None, vector_vector_spectrum_effect)
vector_vector_spectrum_effect.__getitem__ = new_instancemethod(_spectrum_effect.vector_vector_spectrum_effect___getitem__, None, vector_vector_spectrum_effect)
vector_vector_spectrum_effect.__setitem__ = new_instancemethod(_spectrum_effect.vector_vector_spectrum_effect___setitem__, None, vector_vector_spectrum_effect)
vector_vector_spectrum_effect.pop = new_instancemethod(_spectrum_effect.vector_vector_spectrum_effect_pop, None, vector_vector_spectrum_effect)
vector_vector_spectrum_effect.append = new_instancemethod(_spectrum_effect.vector_vector_spectrum_effect_append, None, vector_vector_spectrum_effect)
vector_vector_spectrum_effect.empty = new_instancemethod(_spectrum_effect.vector_vector_spectrum_effect_empty, None, vector_vector_spectrum_effect)
vector_vector_spectrum_effect.size = new_instancemethod(_spectrum_effect.vector_vector_spectrum_effect_size, None, vector_vector_spectrum_effect)
vector_vector_spectrum_effect.swap = new_instancemethod(_spectrum_effect.vector_vector_spectrum_effect_swap, None, vector_vector_spectrum_effect)
vector_vector_spectrum_effect.begin = new_instancemethod(_spectrum_effect.vector_vector_spectrum_effect_begin, None, vector_vector_spectrum_effect)
vector_vector_spectrum_effect.end = new_instancemethod(_spectrum_effect.vector_vector_spectrum_effect_end, None, vector_vector_spectrum_effect)
vector_vector_spectrum_effect.rbegin = new_instancemethod(_spectrum_effect.vector_vector_spectrum_effect_rbegin, None, vector_vector_spectrum_effect)
vector_vector_spectrum_effect.rend = new_instancemethod(_spectrum_effect.vector_vector_spectrum_effect_rend, None, vector_vector_spectrum_effect)
vector_vector_spectrum_effect.clear = new_instancemethod(_spectrum_effect.vector_vector_spectrum_effect_clear, None, vector_vector_spectrum_effect)
vector_vector_spectrum_effect.get_allocator = new_instancemethod(_spectrum_effect.vector_vector_spectrum_effect_get_allocator, None, vector_vector_spectrum_effect)
vector_vector_spectrum_effect.pop_back = new_instancemethod(_spectrum_effect.vector_vector_spectrum_effect_pop_back, None, vector_vector_spectrum_effect)
vector_vector_spectrum_effect.erase = new_instancemethod(_spectrum_effect.vector_vector_spectrum_effect_erase, None, vector_vector_spectrum_effect)
vector_vector_spectrum_effect.push_back = new_instancemethod(_spectrum_effect.vector_vector_spectrum_effect_push_back, None, vector_vector_spectrum_effect)
vector_vector_spectrum_effect.front = new_instancemethod(_spectrum_effect.vector_vector_spectrum_effect_front, None, vector_vector_spectrum_effect)
vector_vector_spectrum_effect.back = new_instancemethod(_spectrum_effect.vector_vector_spectrum_effect_back, None, vector_vector_spectrum_effect)
vector_vector_spectrum_effect.assign = new_instancemethod(_spectrum_effect.vector_vector_spectrum_effect_assign, None, vector_vector_spectrum_effect)
vector_vector_spectrum_effect.resize = new_instancemethod(_spectrum_effect.vector_vector_spectrum_effect_resize, None, vector_vector_spectrum_effect)
vector_vector_spectrum_effect.insert = new_instancemethod(_spectrum_effect.vector_vector_spectrum_effect_insert, None, vector_vector_spectrum_effect)
vector_vector_spectrum_effect.reserve = new_instancemethod(_spectrum_effect.vector_vector_spectrum_effect_reserve, None, vector_vector_spectrum_effect)
vector_vector_spectrum_effect.capacity = new_instancemethod(_spectrum_effect.vector_vector_spectrum_effect_capacity, None, vector_vector_spectrum_effect)
vector_vector_spectrum_effect_swigregister = _spectrum_effect.vector_vector_spectrum_effect_swigregister
vector_vector_spectrum_effect_swigregister(vector_vector_spectrum_effect)



