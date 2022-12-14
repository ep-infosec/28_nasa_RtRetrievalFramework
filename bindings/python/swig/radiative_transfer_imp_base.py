# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _radiative_transfer_imp_base.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_radiative_transfer_imp_base')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_radiative_transfer_imp_base')
    _radiative_transfer_imp_base = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_radiative_transfer_imp_base', [dirname(__file__)])
        except ImportError:
            import _radiative_transfer_imp_base
            return _radiative_transfer_imp_base
        try:
            _mod = imp.load_module('_radiative_transfer_imp_base', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _radiative_transfer_imp_base = swig_import_helper()
    del swig_import_helper
else:
    import _radiative_transfer_imp_base
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


SHARED_PTR_DISOWN = _radiative_transfer_imp_base.SHARED_PTR_DISOWN

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

import full_physics_swig.radiative_transfer_retrievable
import full_physics_swig.radiative_transfer
import full_physics_swig.generic_object
import full_physics_swig.state_vector
import full_physics_swig.sub_state_vector_array
class RadiativeTransferImpBase(full_physics_swig.radiative_transfer_retrievable.SubStateVectorArrayRadiativeTransfer):
    """

    As a design principle, we have each base class with the absolutely
    minimum interface needed for use from the rest of the system.

    This allows us to support any future code that supports this minimum
    interface.

    However, almost always you will want to derive from this class
    instead. See PressureImpBase for a more complete discussion of this.

    C++ includes: radiative_transfer_imp_base.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    __swig_destroy__ = _radiative_transfer_imp_base.delete_RadiativeTransferImpBase

    def clone(self):
        """

        virtual boost::shared_ptr<RadiativeTransferRetrievable> FullPhysics::RadiativeTransferImpBase::clone() const =0

        """
        return _radiative_transfer_imp_base.RadiativeTransferImpBase_clone(self)


    @property
    def number_stokes(self):
        return self._v_number_stokes()


    @property
    def number_spectrometer(self):
        return self._v_number_spectrometer()


    def reflectance(self, Spec_domain, Spec_index, Skip_jacobian=False):
        """

        virtual boost::shared_ptr<Spectrum> FullPhysics::RadiativeTransferImpBase::reflectance_ptr(const SpectralDomain &Spec_domain, int Spec_index, bool
        Skip_jacobian=false) const =0
        For the sake of being able to return a Spectrum class from Python The
        reflectance_ptr method here serves the purpose that the radiance
        method normally would.

        The reflectance method in this implementation simply calls the
        reflectance_ptr method for doing the actual work. 
        """
        return _radiative_transfer_imp_base.RadiativeTransferImpBase_reflectance(self, Spec_domain, Spec_index, Skip_jacobian)


    def print_desc(self, Os):
        """

        virtual void FullPhysics::RadiativeTransferImpBase::print(std::ostream &Os, bool Short_form=false) const
        Print to stream.

        The default calls the function "desc" that returns a string. This
        gives cleaner interface for deriving from this class in python, but
        most C++ classes will want to override this function rather than using
        desc. 
        """
        return _radiative_transfer_imp_base.RadiativeTransferImpBase_print_desc(self, Os)


    def _v_desc(self):
        """

        virtual std::string FullPhysics::RadiativeTransferImpBase::desc() const
        Description of object, to be printed to stream.

        This gives a cleaner interface for deriving from python. 
        """
        return _radiative_transfer_imp_base.RadiativeTransferImpBase__v_desc(self)


    @property
    def desc(self):
        return self._v_desc()


    def __init__(self, *args):
        if self.__class__ == RadiativeTransferImpBase:
            _self = None
        else:
            _self = self
        _radiative_transfer_imp_base.RadiativeTransferImpBase_swiginit(self, _radiative_transfer_imp_base.new_RadiativeTransferImpBase(_self, *args))
    def __disown__(self):
        self.this.disown()
        _radiative_transfer_imp_base.disown_RadiativeTransferImpBase(self)
        return weakref_proxy(self)
RadiativeTransferImpBase.clone = new_instancemethod(_radiative_transfer_imp_base.RadiativeTransferImpBase_clone, None, RadiativeTransferImpBase)
RadiativeTransferImpBase._v_number_stokes = new_instancemethod(_radiative_transfer_imp_base.RadiativeTransferImpBase__v_number_stokes, None, RadiativeTransferImpBase)
RadiativeTransferImpBase._v_number_spectrometer = new_instancemethod(_radiative_transfer_imp_base.RadiativeTransferImpBase__v_number_spectrometer, None, RadiativeTransferImpBase)
RadiativeTransferImpBase.reflectance = new_instancemethod(_radiative_transfer_imp_base.RadiativeTransferImpBase_reflectance, None, RadiativeTransferImpBase)
RadiativeTransferImpBase.stokes = new_instancemethod(_radiative_transfer_imp_base.RadiativeTransferImpBase_stokes, None, RadiativeTransferImpBase)
RadiativeTransferImpBase.stokes_and_jacobian = new_instancemethod(_radiative_transfer_imp_base.RadiativeTransferImpBase_stokes_and_jacobian, None, RadiativeTransferImpBase)
RadiativeTransferImpBase.add_observer = new_instancemethod(_radiative_transfer_imp_base.RadiativeTransferImpBase_add_observer, None, RadiativeTransferImpBase)
RadiativeTransferImpBase.remove_observer = new_instancemethod(_radiative_transfer_imp_base.RadiativeTransferImpBase_remove_observer, None, RadiativeTransferImpBase)
RadiativeTransferImpBase.update_sub_state_hook = new_instancemethod(_radiative_transfer_imp_base.RadiativeTransferImpBase_update_sub_state_hook, None, RadiativeTransferImpBase)
RadiativeTransferImpBase.print_desc = new_instancemethod(_radiative_transfer_imp_base.RadiativeTransferImpBase_print_desc, None, RadiativeTransferImpBase)
RadiativeTransferImpBase._v_desc = new_instancemethod(_radiative_transfer_imp_base.RadiativeTransferImpBase__v_desc, None, RadiativeTransferImpBase)
RadiativeTransferImpBase.mark_used = new_instancemethod(_radiative_transfer_imp_base.RadiativeTransferImpBase_mark_used, None, RadiativeTransferImpBase)
RadiativeTransferImpBase.state_vector_name = new_instancemethod(_radiative_transfer_imp_base.RadiativeTransferImpBase_state_vector_name, None, RadiativeTransferImpBase)
RadiativeTransferImpBase.notify_update = new_instancemethod(_radiative_transfer_imp_base.RadiativeTransferImpBase_notify_update, None, RadiativeTransferImpBase)
RadiativeTransferImpBase.notify_add = new_instancemethod(_radiative_transfer_imp_base.RadiativeTransferImpBase_notify_add, None, RadiativeTransferImpBase)
RadiativeTransferImpBase.notify_remove = new_instancemethod(_radiative_transfer_imp_base.RadiativeTransferImpBase_notify_remove, None, RadiativeTransferImpBase)
RadiativeTransferImpBase.update_sub_state = new_instancemethod(_radiative_transfer_imp_base.RadiativeTransferImpBase_update_sub_state, None, RadiativeTransferImpBase)
RadiativeTransferImpBase.state_vector_name_i = new_instancemethod(_radiative_transfer_imp_base.RadiativeTransferImpBase_state_vector_name_i, None, RadiativeTransferImpBase)
RadiativeTransferImpBase.state_vector_name_sub = new_instancemethod(_radiative_transfer_imp_base.RadiativeTransferImpBase_state_vector_name_sub, None, RadiativeTransferImpBase)
RadiativeTransferImpBase_swigregister = _radiative_transfer_imp_base.RadiativeTransferImpBase_swigregister
RadiativeTransferImpBase_swigregister(RadiativeTransferImpBase)



