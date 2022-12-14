# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _double_with_unit.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_double_with_unit')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_double_with_unit')
    _double_with_unit = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_double_with_unit', [dirname(__file__)])
        except ImportError:
            import _double_with_unit
            return _double_with_unit
        try:
            _mod = imp.load_module('_double_with_unit', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _double_with_unit = swig_import_helper()
    del swig_import_helper
else:
    import _double_with_unit
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


SHARED_PTR_DISOWN = _double_with_unit.SHARED_PTR_DISOWN

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
class DoubleWithUnit(full_physics_swig.generic_object.GenericObject):
    """

    We frequently have a double with units associated with it.

    This is a simple structure that just keeps these two things together.

    C++ includes: double_with_unit.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """

        FullPhysics::DoubleWithUnit::DoubleWithUnit(double V)

        """
        _double_with_unit.DoubleWithUnit_swiginit(self, _double_with_unit.new_DoubleWithUnit(*args))

    def __itruediv__(self, *args):
        return _double_with_unit.DoubleWithUnit___itruediv__(self, *args)
    __idiv__ = __itruediv__



    def convert(self, *args):
        """

        DoubleWithUnit FullPhysics::DoubleWithUnit::convert(const Unit &R) const
        Convert to the given units. 
        """
        return _double_with_unit.DoubleWithUnit_convert(self, *args)


    def convert_wave(self, *args):
        """

        DoubleWithUnit DoubleWithUnit::convert_wave(const Unit &R, const SpectralDomain &Pixel_grid) const
        Variation of convert_wave that also handles the units of sample_index.

        """
        return _double_with_unit.DoubleWithUnit_convert_wave(self, *args)


    @property
    def value(self):
      return self._value()

    @value.setter
    def value(self, val):
      self._value_set(val)

    @property
    def units(self):
      return self._units()

    @units.setter
    def units(self,val):
        self._units_set(val)

    __swig_destroy__ = _double_with_unit.delete_DoubleWithUnit
DoubleWithUnit.__str__ = new_instancemethod(_double_with_unit.DoubleWithUnit___str__, None, DoubleWithUnit)
DoubleWithUnit.__imul__ = new_instancemethod(_double_with_unit.DoubleWithUnit___imul__, None, DoubleWithUnit)
DoubleWithUnit.__iadd__ = new_instancemethod(_double_with_unit.DoubleWithUnit___iadd__, None, DoubleWithUnit)
DoubleWithUnit.__isub__ = new_instancemethod(_double_with_unit.DoubleWithUnit___isub__, None, DoubleWithUnit)
DoubleWithUnit.convert = new_instancemethod(_double_with_unit.DoubleWithUnit_convert, None, DoubleWithUnit)
DoubleWithUnit.convert_wave = new_instancemethod(_double_with_unit.DoubleWithUnit_convert_wave, None, DoubleWithUnit)
DoubleWithUnit._value = new_instancemethod(_double_with_unit.DoubleWithUnit__value, None, DoubleWithUnit)
DoubleWithUnit._value_set = new_instancemethod(_double_with_unit.DoubleWithUnit__value_set, None, DoubleWithUnit)
DoubleWithUnit._units = new_instancemethod(_double_with_unit.DoubleWithUnit__units, None, DoubleWithUnit)
DoubleWithUnit._units_set = new_instancemethod(_double_with_unit.DoubleWithUnit__units_set, None, DoubleWithUnit)
DoubleWithUnit.__mul__ = new_instancemethod(_double_with_unit.DoubleWithUnit___mul__, None, DoubleWithUnit)
DoubleWithUnit.__div__ = new_instancemethod(_double_with_unit.DoubleWithUnit___div__, None, DoubleWithUnit)
DoubleWithUnit.__truediv__ = new_instancemethod(_double_with_unit.DoubleWithUnit___truediv__, None, DoubleWithUnit)
DoubleWithUnit.__add__ = new_instancemethod(_double_with_unit.DoubleWithUnit___add__, None, DoubleWithUnit)
DoubleWithUnit.__sub__ = new_instancemethod(_double_with_unit.DoubleWithUnit___sub__, None, DoubleWithUnit)
DoubleWithUnit_swigregister = _double_with_unit.DoubleWithUnit_swigregister
DoubleWithUnit_swigregister(DoubleWithUnit)



