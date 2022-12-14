# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _absorber_vmr_imp_base.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_absorber_vmr_imp_base')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_absorber_vmr_imp_base')
    _absorber_vmr_imp_base = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_absorber_vmr_imp_base', [dirname(__file__)])
        except ImportError:
            import _absorber_vmr_imp_base
            return _absorber_vmr_imp_base
        try:
            _mod = imp.load_module('_absorber_vmr_imp_base', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _absorber_vmr_imp_base = swig_import_helper()
    del swig_import_helper
else:
    import _absorber_vmr_imp_base
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


SHARED_PTR_DISOWN = _absorber_vmr_imp_base.SHARED_PTR_DISOWN

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
import full_physics_swig.sub_state_vector_array
import full_physics_swig.absorber_vmr
class SubStateVectorArrayAbsorberVmr(full_physics_swig.absorber_vmr.AbsorberVmr, full_physics_swig.state_vector.SubStateVectorObserver):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _absorber_vmr_imp_base.delete_SubStateVectorArrayAbsorberVmr

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

SubStateVectorArrayAbsorberVmr.init = new_instancemethod(_absorber_vmr_imp_base.SubStateVectorArrayAbsorberVmr_init, None, SubStateVectorArrayAbsorberVmr)
SubStateVectorArrayAbsorberVmr.state_vector_name_i = new_instancemethod(_absorber_vmr_imp_base.SubStateVectorArrayAbsorberVmr_state_vector_name_i, None, SubStateVectorArrayAbsorberVmr)
SubStateVectorArrayAbsorberVmr.update_sub_state_hook = new_instancemethod(_absorber_vmr_imp_base.SubStateVectorArrayAbsorberVmr_update_sub_state_hook, None, SubStateVectorArrayAbsorberVmr)
SubStateVectorArrayAbsorberVmr._v_coefficient = new_instancemethod(_absorber_vmr_imp_base.SubStateVectorArrayAbsorberVmr__v_coefficient, None, SubStateVectorArrayAbsorberVmr)
SubStateVectorArrayAbsorberVmr._v_used_flag_value = new_instancemethod(_absorber_vmr_imp_base.SubStateVectorArrayAbsorberVmr__v_used_flag_value, None, SubStateVectorArrayAbsorberVmr)
SubStateVectorArrayAbsorberVmr._v_statevector_covariance = new_instancemethod(_absorber_vmr_imp_base.SubStateVectorArrayAbsorberVmr__v_statevector_covariance, None, SubStateVectorArrayAbsorberVmr)
SubStateVectorArrayAbsorberVmr._v_pressure = new_instancemethod(_absorber_vmr_imp_base.SubStateVectorArrayAbsorberVmr__v_pressure, None, SubStateVectorArrayAbsorberVmr)
SubStateVectorArrayAbsorberVmr_swigregister = _absorber_vmr_imp_base.SubStateVectorArrayAbsorberVmr_swigregister
SubStateVectorArrayAbsorberVmr_swigregister(SubStateVectorArrayAbsorberVmr)

class AbsorberVmrImpBase(SubStateVectorArrayAbsorberVmr):
    """

    As a design principle, we have each base class with the absolutely
    minimum interface needed for use from the rest of the system.

    This allows us to support any future code that supports this minimum
    interface.

    However, almost always you will want to derive from this class
    instead. See PressureImpBase for a more complete discussion of this.

    C++ includes: absorber_vmr_imp_base.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    __swig_destroy__ = _absorber_vmr_imp_base.delete_AbsorberVmrImpBase

    def clone(self, *args):
        """

        virtual boost::shared_ptr<AbsorberVmr> FullPhysics::AbsorberVmrImpBase::clone(const boost::shared_ptr< Pressure > &Press) const =0

        """
        return _absorber_vmr_imp_base.AbsorberVmrImpBase_clone(self, *args)


    def _v_gas_name(self):
        """

        virtual std::string FullPhysics::AbsorberVmrImpBase::gas_name() const

        """
        return _absorber_vmr_imp_base.AbsorberVmrImpBase__v_gas_name(self)


    @property
    def gas_name(self):
        return self._v_gas_name()


    def volume_mixing_ratio(self, P):
        """

        virtual AutoDerivative<double> FullPhysics::AbsorberVmrImpBase::volume_mixing_ratio(const AutoDerivative< double > &P) const

        """
        return _absorber_vmr_imp_base.AbsorberVmrImpBase_volume_mixing_ratio(self, P)


    def _v_state_used(self):
        """

        virtual blitz::Array<bool, 1> FullPhysics::AbsorberVmrImpBase::state_used() const

        """
        return _absorber_vmr_imp_base.AbsorberVmrImpBase__v_state_used(self)


    @property
    def state_used(self):
        return self._v_state_used()


    def update_sub_state_hook(self):
        """

        virtual void FullPhysics::AbsorberVmrImpBase::update_sub_state_hook()

        """
        return _absorber_vmr_imp_base.AbsorberVmrImpBase_update_sub_state_hook(self)


    def print_desc(self, Os):
        """

        virtual void FullPhysics::AbsorberVmrImpBase::print(std::ostream &Os) const
        Print to stream.

        The default calls the function "desc" that returns a string. This
        gives cleaner interface for deriving from this class in python, but
        most C++ classes will want to override this function rather than using
        desc. 
        """
        return _absorber_vmr_imp_base.AbsorberVmrImpBase_print_desc(self, Os)


    def _v_desc(self):
        """

        virtual std::string FullPhysics::AbsorberVmrImpBase::desc() const
        Description of object, to be printed to stream.

        This gives a cleaner interface for deriving from python. 
        """
        return _absorber_vmr_imp_base.AbsorberVmrImpBase__v_desc(self)


    @property
    def desc(self):
        return self._v_desc()

    cache_stale = _swig_property(_absorber_vmr_imp_base.AbsorberVmrImpBase_cache_stale_get, _absorber_vmr_imp_base.AbsorberVmrImpBase_cache_stale_set)
    vmr = _swig_property(_absorber_vmr_imp_base.AbsorberVmrImpBase_vmr_get, _absorber_vmr_imp_base.AbsorberVmrImpBase_vmr_set)

    def __init__(self, Gas_name, Coeff, Used_flag, Press, Mark_according_to_press=True, Pdep_start=0):
        if self.__class__ == AbsorberVmrImpBase:
            _self = None
        else:
            _self = self
        _absorber_vmr_imp_base.AbsorberVmrImpBase_swiginit(self, _absorber_vmr_imp_base.new_AbsorberVmrImpBase(_self, Gas_name, Coeff, Used_flag, Press, Mark_according_to_press, Pdep_start))
    def __disown__(self):
        self.this.disown()
        _absorber_vmr_imp_base.disown_AbsorberVmrImpBase(self)
        return weakref_proxy(self)
AbsorberVmrImpBase.clone = new_instancemethod(_absorber_vmr_imp_base.AbsorberVmrImpBase_clone, None, AbsorberVmrImpBase)
AbsorberVmrImpBase._v_gas_name = new_instancemethod(_absorber_vmr_imp_base.AbsorberVmrImpBase__v_gas_name, None, AbsorberVmrImpBase)
AbsorberVmrImpBase.volume_mixing_ratio = new_instancemethod(_absorber_vmr_imp_base.AbsorberVmrImpBase_volume_mixing_ratio, None, AbsorberVmrImpBase)
AbsorberVmrImpBase._v_state_used = new_instancemethod(_absorber_vmr_imp_base.AbsorberVmrImpBase__v_state_used, None, AbsorberVmrImpBase)
AbsorberVmrImpBase.add_observer = new_instancemethod(_absorber_vmr_imp_base.AbsorberVmrImpBase_add_observer, None, AbsorberVmrImpBase)
AbsorberVmrImpBase.remove_observer = new_instancemethod(_absorber_vmr_imp_base.AbsorberVmrImpBase_remove_observer, None, AbsorberVmrImpBase)
AbsorberVmrImpBase.update_sub_state_hook = new_instancemethod(_absorber_vmr_imp_base.AbsorberVmrImpBase_update_sub_state_hook, None, AbsorberVmrImpBase)
AbsorberVmrImpBase.print_desc = new_instancemethod(_absorber_vmr_imp_base.AbsorberVmrImpBase_print_desc, None, AbsorberVmrImpBase)
AbsorberVmrImpBase._v_desc = new_instancemethod(_absorber_vmr_imp_base.AbsorberVmrImpBase__v_desc, None, AbsorberVmrImpBase)
AbsorberVmrImpBase.mark_used = new_instancemethod(_absorber_vmr_imp_base.AbsorberVmrImpBase_mark_used, None, AbsorberVmrImpBase)
AbsorberVmrImpBase.state_vector_name = new_instancemethod(_absorber_vmr_imp_base.AbsorberVmrImpBase_state_vector_name, None, AbsorberVmrImpBase)
AbsorberVmrImpBase.notify_update = new_instancemethod(_absorber_vmr_imp_base.AbsorberVmrImpBase_notify_update, None, AbsorberVmrImpBase)
AbsorberVmrImpBase.notify_add = new_instancemethod(_absorber_vmr_imp_base.AbsorberVmrImpBase_notify_add, None, AbsorberVmrImpBase)
AbsorberVmrImpBase.notify_remove = new_instancemethod(_absorber_vmr_imp_base.AbsorberVmrImpBase_notify_remove, None, AbsorberVmrImpBase)
AbsorberVmrImpBase.update_sub_state = new_instancemethod(_absorber_vmr_imp_base.AbsorberVmrImpBase_update_sub_state, None, AbsorberVmrImpBase)
AbsorberVmrImpBase.state_vector_name_i = new_instancemethod(_absorber_vmr_imp_base.AbsorberVmrImpBase_state_vector_name_i, None, AbsorberVmrImpBase)
AbsorberVmrImpBase.state_vector_name_sub = new_instancemethod(_absorber_vmr_imp_base.AbsorberVmrImpBase_state_vector_name_sub, None, AbsorberVmrImpBase)
AbsorberVmrImpBase.calc_vmr = new_instancemethod(_absorber_vmr_imp_base.AbsorberVmrImpBase_calc_vmr, None, AbsorberVmrImpBase)
AbsorberVmrImpBase_swigregister = _absorber_vmr_imp_base.AbsorberVmrImpBase_swigregister
AbsorberVmrImpBase_swigregister(AbsorberVmrImpBase)



