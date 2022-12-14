# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _ils_function.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_ils_function')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_ils_function')
    _ils_function = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_ils_function', [dirname(__file__)])
        except ImportError:
            import _ils_function
            return _ils_function
        try:
            _mod = imp.load_module('_ils_function', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _ils_function = swig_import_helper()
    del swig_import_helper
else:
    import _ils_function
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


SHARED_PTR_DISOWN = _ils_function.SHARED_PTR_DISOWN

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
class ObservableIlsFunction(full_physics_swig.generic_object.GenericObject):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _ils_function.delete_ObservableIlsFunction
ObservableIlsFunction.add_observer_and_keep_reference = new_instancemethod(_ils_function.ObservableIlsFunction_add_observer_and_keep_reference, None, ObservableIlsFunction)
ObservableIlsFunction.add_observer = new_instancemethod(_ils_function.ObservableIlsFunction_add_observer, None, ObservableIlsFunction)
ObservableIlsFunction.remove_observer = new_instancemethod(_ils_function.ObservableIlsFunction_remove_observer, None, ObservableIlsFunction)
ObservableIlsFunction_swigregister = _ils_function.ObservableIlsFunction_swigregister
ObservableIlsFunction_swigregister(ObservableIlsFunction)

class ObserverIlsFunction(full_physics_swig.generic_object.GenericObject):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self):
        _ils_function.ObserverIlsFunction_swiginit(self, _ils_function.new_ObserverIlsFunction())
    __swig_destroy__ = _ils_function.delete_ObserverIlsFunction
ObserverIlsFunction.notify_update = new_instancemethod(_ils_function.ObserverIlsFunction_notify_update, None, ObserverIlsFunction)
ObserverIlsFunction.notify_add = new_instancemethod(_ils_function.ObserverIlsFunction_notify_add, None, ObserverIlsFunction)
ObserverIlsFunction.notify_remove = new_instancemethod(_ils_function.ObserverIlsFunction_notify_remove, None, ObserverIlsFunction)
ObserverIlsFunction_swigregister = _ils_function.ObserverIlsFunction_swigregister
ObserverIlsFunction_swigregister(ObserverIlsFunction)

class IlsFunction(full_physics_swig.state_vector.StateVectorObserver, ObservableIlsFunction):
    """

    This class models an Instrument Line Shape (ILS) function.

    This returns the response around a given wave number, for a given set
    of wavenumbers. This class is use by IlsConvolution.

    It is not guaranteed that the function is normalized, the calling
    class should normalize this if needed.

    C++ includes: ils_function.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _ils_function.delete_IlsFunction

    def ils(self, wn_center, wn, OUTPUT, jac_optimization=False):
        """

        virtual void FullPhysics::IlsFunction::ils(const AutoDerivative< double > &wn_center, const blitz::Array<
        double, 1 > &wn, ArrayAd< double, 1 > &res, bool
        jacobian_optimization=false) const =0
        Return response function.

        Note that is function turns out to be a bit of a bottle neck because
        it is called so many times. Most of the time the results are the same
        size from one call to the next, so we pass in the results rather than
        having this be a return value like we normally do. This avoids
        recreating the array multiple times. We resize the output, so it is
        fine if it doesn't happen to be the final result size. But much of the
        time we avoid and extra allocation and destruction.

        An important optimization is done in IlsConvolution, where instead of
        calculating dres/dstate we create a short gradient [dwn_center,
        dscale]. IlsConvolution then applies the chain rule to get the final
        results in dstate. The flag "jac_optimization" controls this.

        Parameters:
        -----------

        wn_center:  The wave number of the center of the response function

        wn:  The wavenumbers to return response function for.

        res:  Return the response function for each of the wn value.
        jacobian_optimization If true, then do the optimization described in
        this function. 
        """
        return _ils_function.IlsFunction_ils(self, wn_center, wn, OUTPUT, jac_optimization)


    def _v_band_name(self):
        """

        virtual std::string FullPhysics::IlsFunction::band_name() const =0
        Descriptive name of the band. 
        """
        return _ils_function.IlsFunction__v_band_name(self)


    @property
    def band_name(self):
        return self._v_band_name()


    def _v_hdf_band_name(self):
        """

        virtual std::string FullPhysics::IlsFunction::hdf_band_name() const
        In general, the name used in HDF files for a particular band is
        similar but not identical to the more human readable band_name.

        For example, with GOSAT we use the HDF field name "weak_co2", but
        the band name is "WC-Band". This gives the HDF name to use.

        The default implementation just returns the same string as the band
        name. 
        """
        return _ils_function.IlsFunction__v_hdf_band_name(self)


    @property
    def hdf_band_name(self):
        return self._v_hdf_band_name()

IlsFunction.ils = new_instancemethod(_ils_function.IlsFunction_ils, None, IlsFunction)
IlsFunction._v_band_name = new_instancemethod(_ils_function.IlsFunction__v_band_name, None, IlsFunction)
IlsFunction._v_hdf_band_name = new_instancemethod(_ils_function.IlsFunction__v_hdf_band_name, None, IlsFunction)
IlsFunction_swigregister = _ils_function.IlsFunction_swigregister
IlsFunction_swigregister(IlsFunction)

class SubStateVectorArrayIlsFunction(IlsFunction, full_physics_swig.state_vector.SubStateVectorObserver):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _ils_function.delete_SubStateVectorArrayIlsFunction

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

SubStateVectorArrayIlsFunction.init = new_instancemethod(_ils_function.SubStateVectorArrayIlsFunction_init, None, SubStateVectorArrayIlsFunction)
SubStateVectorArrayIlsFunction.state_vector_name_i = new_instancemethod(_ils_function.SubStateVectorArrayIlsFunction_state_vector_name_i, None, SubStateVectorArrayIlsFunction)
SubStateVectorArrayIlsFunction.update_sub_state_hook = new_instancemethod(_ils_function.SubStateVectorArrayIlsFunction_update_sub_state_hook, None, SubStateVectorArrayIlsFunction)
SubStateVectorArrayIlsFunction._v_coefficient = new_instancemethod(_ils_function.SubStateVectorArrayIlsFunction__v_coefficient, None, SubStateVectorArrayIlsFunction)
SubStateVectorArrayIlsFunction._v_used_flag_value = new_instancemethod(_ils_function.SubStateVectorArrayIlsFunction__v_used_flag_value, None, SubStateVectorArrayIlsFunction)
SubStateVectorArrayIlsFunction._v_statevector_covariance = new_instancemethod(_ils_function.SubStateVectorArrayIlsFunction__v_statevector_covariance, None, SubStateVectorArrayIlsFunction)
SubStateVectorArrayIlsFunction._v_pressure = new_instancemethod(_ils_function.SubStateVectorArrayIlsFunction__v_pressure, None, SubStateVectorArrayIlsFunction)
SubStateVectorArrayIlsFunction_swigregister = _ils_function.SubStateVectorArrayIlsFunction_swigregister
SubStateVectorArrayIlsFunction_swigregister(SubStateVectorArrayIlsFunction)



