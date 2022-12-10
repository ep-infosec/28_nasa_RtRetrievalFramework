# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _gas_vmr_apriori.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_gas_vmr_apriori')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_gas_vmr_apriori')
    _gas_vmr_apriori = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_gas_vmr_apriori', [dirname(__file__)])
        except ImportError:
            import _gas_vmr_apriori
            return _gas_vmr_apriori
        try:
            _mod = imp.load_module('_gas_vmr_apriori', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _gas_vmr_apriori = swig_import_helper()
    del swig_import_helper
else:
    import _gas_vmr_apriori
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


SHARED_PTR_DISOWN = _gas_vmr_apriori.SHARED_PTR_DISOWN

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
class GasVmrApriori(full_physics_swig.generic_object.GenericObject):
    """

    Adapts the ReferenceVmrApriori class into a form that is easier to
    work with in the context of how this framework works.

    This class deals keys off of pressure levels like the rest of the
    framework. It also uses the increasing pressure levels convention.

    The VMR returned will be in the order of levels expected elsewhere in
    the framework.

    C++ includes: gas_vmr_apriori.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, Met_file, L1b_file, Alt, Hdf_static_input, Hdf_group, Gas_name, temp_avg_window):
        """

        GasVmrApriori::GasVmrApriori(const boost::shared_ptr< Meteorology > &Met_file, const
        boost::shared_ptr< Level1b > &L1b_file, const boost::shared_ptr<
        Altitude > &Alt, const HdfFile &Hdf_static_input, const std::string
        &Hdf_group, const std::string &Gas_name, const int temp_avg_window=11)

        """
        _gas_vmr_apriori.GasVmrApriori_swiginit(self, _gas_vmr_apriori.new_GasVmrApriori(Met_file, L1b_file, Alt, Hdf_static_input, Hdf_group, Gas_name, temp_avg_window))

    @property
    def apriori_vmr(self):
        return self._v_apriori_vmr()


    def _v_apriori_vmr(self, *args):
        """

        const blitz::Array< double, 1 > GasVmrApriori::apriori_vmr(const Pressure &pressure) const

        """
        return _gas_vmr_apriori.GasVmrApriori__v_apriori_vmr(self, *args)


    def _v_reference(self):
        """

        const boost::shared_ptr<ReferenceVmrApriori> FullPhysics::GasVmrApriori::reference() const

        """
        return _gas_vmr_apriori.GasVmrApriori__v_reference(self)


    @property
    def reference(self):
        return self._v_reference()


    def _v_tropopause_altitude(self):
        """

        const DoubleWithUnit FullPhysics::GasVmrApriori::tropopause_altitude() const

        """
        return _gas_vmr_apriori.GasVmrApriori__v_tropopause_altitude(self)


    @property
    def tropopause_altitude(self):
        return self._v_tropopause_altitude()


    def _v_tropopause_pressure(self):
        """

        const double GasVmrApriori::tropopause_pressure() const

        """
        return _gas_vmr_apriori.GasVmrApriori__v_tropopause_pressure(self)


    @property
    def tropopause_pressure(self):
        return self._v_tropopause_pressure()

    __swig_destroy__ = _gas_vmr_apriori.delete_GasVmrApriori
GasVmrApriori._v_apriori_vmr = new_instancemethod(_gas_vmr_apriori.GasVmrApriori__v_apriori_vmr, None, GasVmrApriori)
GasVmrApriori._v_reference = new_instancemethod(_gas_vmr_apriori.GasVmrApriori__v_reference, None, GasVmrApriori)
GasVmrApriori._v_tropopause_altitude = new_instancemethod(_gas_vmr_apriori.GasVmrApriori__v_tropopause_altitude, None, GasVmrApriori)
GasVmrApriori._v_tropopause_pressure = new_instancemethod(_gas_vmr_apriori.GasVmrApriori__v_tropopause_pressure, None, GasVmrApriori)
GasVmrApriori.__str__ = new_instancemethod(_gas_vmr_apriori.GasVmrApriori___str__, None, GasVmrApriori)
GasVmrApriori_swigregister = _gas_vmr_apriori.GasVmrApriori_swigregister
GasVmrApriori_swigregister(GasVmrApriori)



