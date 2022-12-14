# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _hdf_sounding_id.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_hdf_sounding_id')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_hdf_sounding_id')
    _hdf_sounding_id = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_hdf_sounding_id', [dirname(__file__)])
        except ImportError:
            import _hdf_sounding_id
            return _hdf_sounding_id
        try:
            _mod = imp.load_module('_hdf_sounding_id', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _hdf_sounding_id = swig_import_helper()
    del swig_import_helper
else:
    import _hdf_sounding_id
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


SHARED_PTR_DISOWN = _hdf_sounding_id.SHARED_PTR_DISOWN

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
class HdfSoundingId(full_physics_swig.generic_object.GenericObject):
    """

    This class defines the interface for a sounding id referring to data
    within an HDF file.

    This amounts to translating a string into frame and sounding indexes
    where data should be read from the HDF files. The details of the exact
    meaning of the string and how the indexing is computed may differ from
    file type to file type.

    C++ includes: hdf_sounding_id.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __swig_destroy__ = _hdf_sounding_id.delete_HdfSoundingId

    def _v_frame_number(self):
        """

        virtual int FullPhysics::HdfSoundingId::frame_number() const

        """
        return _hdf_sounding_id.HdfSoundingId__v_frame_number(self)


    @property
    def frame_number(self):
        return self._v_frame_number()


    def _v_sounding_number(self):
        """

        virtual int FullPhysics::HdfSoundingId::sounding_number() const

        """
        return _hdf_sounding_id.HdfSoundingId__v_sounding_number(self)


    @property
    def sounding_number(self):
        return self._v_sounding_number()


    def _v_sounding_id(self):
        """

        virtual int64_t FullPhysics::HdfSoundingId::sounding_id() const

        """
        return _hdf_sounding_id.HdfSoundingId__v_sounding_id(self)


    @property
    def sounding_id(self):
        return self._v_sounding_id()

HdfSoundingId._v_frame_number = new_instancemethod(_hdf_sounding_id.HdfSoundingId__v_frame_number, None, HdfSoundingId)
HdfSoundingId._v_sounding_number = new_instancemethod(_hdf_sounding_id.HdfSoundingId__v_sounding_number, None, HdfSoundingId)
HdfSoundingId._v_sounding_id = new_instancemethod(_hdf_sounding_id.HdfSoundingId__v_sounding_id, None, HdfSoundingId)
HdfSoundingId.__str__ = new_instancemethod(_hdf_sounding_id.HdfSoundingId___str__, None, HdfSoundingId)
HdfSoundingId_swigregister = _hdf_sounding_id.HdfSoundingId_swigregister
HdfSoundingId_swigregister(HdfSoundingId)



