# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _model_measure.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_model_measure')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_model_measure')
    _model_measure = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_model_measure', [dirname(__file__)])
        except ImportError:
            import _model_measure
            return _model_measure
        try:
            _mod = imp.load_module('_model_measure', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _model_measure = swig_import_helper()
    del swig_import_helper
else:
    import _model_measure
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


SHARED_PTR_DISOWN = _model_measure.SHARED_PTR_DISOWN

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

import full_physics_swig.model_state
import full_physics_swig.problem_state
import full_physics_swig.generic_object
class ModelMeasure(full_physics_swig.model_state.ModelState):
    """

    The base class for models and measurements.

    This interface class is designed for the purpose of fitting a
    parametrized mathematical model (a vector function) to the measured
    data. The class hierarchy rooted at this base class implements three
    components that are needed for the fitting process: The mathematical
    model (vector) and its Jacobian

    The measurement (vector) and its error covariance matrix

    The statistical analysis method for model fitting

    The class hierarchy rooted at ModelMeasure is designed assuming only
    one of the following two statistical analysis methods: Maximum
    Likelihood

    Maximum A Posteriori

    Assuming only the above two statistical analysis methods, this class
    is designed to be the common interface needed to implement the two
    statistical methods mentioned above. Therefore, in the light of some
    other statistical analysis method, that I don't know about it, it may
    or may not be better to redesign this class hierarchy in some other
    way.

    The parameter handling capability of this class is inherited from
    ProblemState class (through direct or indirect inheritance). However,
    most real-life mathematical models and their Jacobians are
    computationally expensive; therefore, this class inherits ModelState
    from ProblemState class hierarchy to inherit the capability of storing
    and possibly reusing the last evaluations of the model and its
    Jacobian.

    The measurement error covariance matrix is not necessarily a diagonal
    matrix; however, in the implementation of this class it is assumed to
    be a diagonal matrix.

    C++ includes: model_measure.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _model_measure.delete_ModelMeasure

    def model_eval(self):
        """

        virtual void FullPhysics::ModelMeasure::model_eval()=0
        Evaluates the model at the currently set parameter values.

        This method must be implemented by the classes derived from this
        class.

        The parameters (the point in the parameter space) must have already
        been set before calling this method. The parameters are already set if
        one of the following methods is already called successfully:
        parameters() (see ProblemState class)

        model_x() (see CostFunc class)

        jacobian_x()

        model_jacobian_x()

        If the parameters are already set, then this method evaluate the model
        at the currently set parameter values (point in the parameter space).

        """
        return _model_measure.ModelMeasure_model_eval(self)


    def _v_model(self):
        """

        virtual blitz::Array<double, 1> FullPhysics::ModelMeasure::model()
        Evaluates and returns the model at the currently set parameter values.

        All the comments on model_eval() method also apply to this method, and
        in addition this method returns the evaluated model.

        The size of the model vector can be obtained in advance by calling
        measurement_size().

        Evaluated model at the current point 
        """
        return _model_measure.ModelMeasure__v_model(self)


    @property
    def model(self):
        return self._v_model()


    def model_x(self, x):
        """

        virtual blitz::Array<double, 1> FullPhysics::ModelMeasure::model_x(const blitz::Array< double, 1 > &x)
        The model function with parameters.

        This method also evaluates the model; however, it sets the model at
        the input new point and then evaluates the model.

        The size of the model vector can be obtained in advance by calling
        measurement_size().

        Parameters:
        -----------

        x:  New set of parameters

        Evaluated model at the input new point 
        """
        return _model_measure.ModelMeasure_model_x(self, x)


    def jacobian_eval(self):
        """

        virtual void FullPhysics::ModelMeasure::jacobian_eval()=0
        Evaluates the Jacobian of the model at the currently set parameter
        values.

        This method must be implemented by the classes derived from this
        class.

        The parameters (the point in the parameter space) must have already
        been set before calling this method. The parameters are already set if
        one of the following methods is already called successfully:
        parameters() (see ProblemState class)

        model_x() (see CostFunc class)

        jacobian_x()

        model_jacobian_x()

        If the parameters are already set, then this method evaluate the
        Jacobian of the model at the currently set parameter values (point in
        the parameter space). 
        """
        return _model_measure.ModelMeasure_jacobian_eval(self)


    def _v_jacobian(self):
        """

        virtual blitz::Array<double, 2> FullPhysics::ModelMeasure::jacobian()
        Evaluates and returns the Jacobian of the model at the currently set
        parameter values.

        All the comments on jacobian_eval() method also apply to this method,
        and in addition this method returns the evaluated Jacobian.

        The sizes of the Jacobian matrix can be obtained in advance: For the
        number of its rows call measurement_size().

        For the number of its columns call expected_parameter_size() (see
        ProblemState class).

        Evaluated model Jacobian at the current point 
        """
        return _model_measure.ModelMeasure__v_jacobian(self)


    @property
    def jacobian(self):
        return self._v_jacobian()


    def jacobian_x(self, x):
        """

        virtual blitz::Array<double, 2> FullPhysics::ModelMeasure::jacobian_x(const blitz::Array< double, 1 > &x)
        The model Jacobian with parameters.

        This method also evaluates the Jacobian; however, it sets the model at
        the input new point and then evaluates its Jacobian.

        The sizes of the Jacobian matrix can be obtained in advance: For the
        number of its rows call measurement_size().

        For the number of its columns call expected_parameter_size() (see
        ProblemState class).

        Parameters:
        -----------

        x:  New set of parameters

        Evaluated model Jacobian at the input new point 
        """
        return _model_measure.ModelMeasure_jacobian_x(self, x)


    def model_jacobian_eval(self):
        """

        virtual void FullPhysics::ModelMeasure::model_jacobian_eval()
        Evaluates the model and its Jacobian at the currently set parameter
        values.

        The parameters (the point in the parameter space) must have already
        been set before calling this method. The parameters are already set if
        one of the following methods is already called successfully:
        parameters() (see ProblemState class)

        model_x() (see CostFunc class)

        jacobian_x()

        model_jacobian_x()

        If the parameters are already set, then this method evaluate the model
        and its Jacobian at the currently set parameter values (point in the
        parameter space). 
        """
        return _model_measure.ModelMeasure_model_jacobian_eval(self)


    def model_jacobian(self, m, k):
        """

        virtual void FullPhysics::ModelMeasure::model_jacobian(blitz::Array< double, 1 > &m, blitz::Array< double, 2 > &k)
        Evaluates model and its Jacobian together.

        All the comments on model_jacobian_eval() method also apply to this
        method, and in addition this method passes to the caller the evaluated
        model and its Jacobian.

        Parameters:
        -----------

        m:  The model

        k:  The Jacobian of the model 
        """
        return _model_measure.ModelMeasure_model_jacobian(self, m, k)


    def model_jacobian_x(self, x, m, k):
        """

        virtual void FullPhysics::ModelMeasure::model_jacobian_x(const blitz::Array< double, 1 > &x, blitz::Array< double, 1 > &m,
        blitz::Array< double, 2 > &k)
        Model and its Jacobian with parameters.

        This method passes to the caller the evaluated model and its Jacobian
        after setting the problem at the input new point.

        Parameters:
        -----------

        x:  New set of parameters

        m:  The model

        k:  The Jacobian of the model 
        """
        return _model_measure.ModelMeasure_model_jacobian_x(self, x, m, k)


    def _v_measurement(self):
        """

        virtual blitz::Array<double, 1> FullPhysics::ModelMeasure::measurement() const
        Returns the measured data, to which the model is fit.

        The measurement vector. 
        """
        return _model_measure.ModelMeasure__v_measurement(self)


    @property
    def measurement(self):
        return self._v_measurement()


    def _v_measurement_error_cov(self):
        """

        virtual blitz::Array<double, 1> FullPhysics::ModelMeasure::measurement_error_cov() const
        Returns the measurement error covariance (implemented as a diagonal
        matrix).

        The measurement error covariance. 
        """
        return _model_measure.ModelMeasure__v_measurement_error_cov(self)


    @property
    def measurement_error_cov(self):
        return self._v_measurement_error_cov()


    def _v_measurement_size(self):
        """

        virtual int FullPhysics::ModelMeasure::measurement_size() const
        Returns the size of the measurement data vector.

        This method returns the size of the measured data vector. The
        following must also be equal to the value returned by
        measurement_size(): The size of the model data

        The number of the rows of the model Jacobian

        The number of the diagonal elements of the error covariance matrix

        The size of the measurement data vector 
        """
        return _model_measure.ModelMeasure__v_measurement_size(self)


    @property
    def measurement_size(self):
        return self._v_measurement_size()


    def assert_model_correct(self, m):
        """

        void ModelMeasure::assert_model_correct(const blitz::Array< double, 1 > &m) const
        Conditions that must be satisfied when a derived class computes the
        model.

        This method is just the implementation of some conditions that must be
        satisfied after a derived class computes the model. The derived class
        itself calls this method to check the computed model.

        Parameters:
        -----------

        m:  The computed model 
        """
        return _model_measure.ModelMeasure_assert_model_correct(self, m)


    def assert_jacobian_correct(self, k):
        """

        void ModelMeasure::assert_jacobian_correct(const blitz::Array< double, 2 > &k) const
        Conditions that must be satisfied when a derived class computes the
        Jacobian of the model.

        This method is just the implementation of some conditions that must be
        satisfied after a derived class computes the Jacobian of the model.
        The derived class itself calls this method to check the computed
        Jacobian.

        Parameters:
        -----------

        k:  The computed model 
        """
        return _model_measure.ModelMeasure_assert_jacobian_correct(self, k)


    def _v_model_measure_diff(self):
        """

        virtual blitz::Array<double, 1> FullPhysics::ModelMeasure::model_measure_diff()
        Returns model and measurement difference (model - measurement)

        This method is for convenience. It returns the difference of the
        computed model and the measurement. The difference is not called
        residual on purpose. The term residual will be used in the context of
        the Non-Linear (or Linear) Least Squares optimization.

        Let the following be the computed model and the measured data
        respectively M

        S

        Then this method returns \\[ M - S \\]

        Model and measurement difference (model - measurement) 
        """
        return _model_measure.ModelMeasure__v_model_measure_diff(self)


    @property
    def model_measure_diff(self):
        return self._v_model_measure_diff()


    def _v_uncert_weighted_model_measure_diff(self):
        """

        virtual blitz::Array<double, 1> FullPhysics::ModelMeasure::uncert_weighted_model_measure_diff()
        Returns model and measurement difference weighted by the inverse of
        the Cholesky decomposition of the error covariance matrix.

        This method is for convenience. It returns the difference of the
        computed model and measurement, model_measure_diff(), weighted by the
        Cholesky decomposition (roughly speaking the square root) of the error
        covariance matrix. In the name of this method "uncert" is the short
        for uncertainty, but probably using the word uncertainty or uncert in
        the name of this method is a bad Idea. In the implementation of this
        class the error covariance matrix is implemented as a diagonal matrix.
        However, if the matrix were not diagonal, still the purpose of this
        method would be to weight the model and the measurement difference
        with the Cholesky decomposition of the entire error covariance matrix.

        Let the following be the computed model, the measured data, and the
        measurement error covariance matrix respectively: M

        S

        Se

        Then the Cholesky decomposition of the error covariance matrix is
        \\[ S_e = C_e C_e^T \\] and this method returns \\[
        C_e^{-1}(M-S) \\]

        Model and measurement difference weighted by the inverse of the
        Cholesky decomposition of the error covariance matrix 
        """
        return _model_measure.ModelMeasure__v_uncert_weighted_model_measure_diff(self)


    @property
    def uncert_weighted_model_measure_diff(self):
        return self._v_uncert_weighted_model_measure_diff()


    def _v_uncert_weighted_jacobian(self):
        """

        Array< double, 2 > ModelMeasure::uncert_weighted_jacobian()
        Returns the model Jacobian weighted by the inverse of the Cholesky
        decomposition of the error covariance matrix.

        This method is for convenience. It returns the model Jacobian weighted
        by the Cholesky decomposition (roughly speaking the square root) of
        the error covariance matrix.

        Let the following be the computed model Jacobian and the measurement
        error covariance matrix respectively: K

        Se

        Then the Cholesky decomposition of the error covariance matrix is
        \\[ S_e = C_e C_e^T \\] and this method returns \\[ C_e^{-1}K
        \\]

        The method uncert_weighted_model_measure_diff() is another function of
        the parameters, and the method uncert_weighted_jacobian() is the
        Jacobian of uncert_weighted_model_measure_diff().

        Model Jacobian weighted by the inverse of the Cholesky decomposition
        of the error covariance matrix 
        """
        return _model_measure.ModelMeasure__v_uncert_weighted_jacobian(self)


    @property
    def uncert_weighted_jacobian(self):
        return self._v_uncert_weighted_jacobian()


    def _v_uncert_weighted_jac_inner_product(self):
        """

        Array< double, 2 > ModelMeasure::uncert_weighted_jac_inner_product()
        Returns the inner product of the matrix returned by the method
        uncert_weighted_jacobian() by itself.

        Let the following be the computed model Jacobian and the measurement
        error covariance matrix respectively: K

        Se

        Then this method returns \\[ K^TS_e^{-1}K \\]

        The inner product of the matrix returned by the method
        uncert_weighted_jacobian() by itself. 
        """
        return _model_measure.ModelMeasure__v_uncert_weighted_jac_inner_product(self)


    @property
    def uncert_weighted_jac_inner_product(self):
        return self._v_uncert_weighted_jac_inner_product()

ModelMeasure.model_eval = new_instancemethod(_model_measure.ModelMeasure_model_eval, None, ModelMeasure)
ModelMeasure._v_model = new_instancemethod(_model_measure.ModelMeasure__v_model, None, ModelMeasure)
ModelMeasure.model_x = new_instancemethod(_model_measure.ModelMeasure_model_x, None, ModelMeasure)
ModelMeasure.jacobian_eval = new_instancemethod(_model_measure.ModelMeasure_jacobian_eval, None, ModelMeasure)
ModelMeasure._v_jacobian = new_instancemethod(_model_measure.ModelMeasure__v_jacobian, None, ModelMeasure)
ModelMeasure.jacobian_x = new_instancemethod(_model_measure.ModelMeasure_jacobian_x, None, ModelMeasure)
ModelMeasure.model_jacobian_eval = new_instancemethod(_model_measure.ModelMeasure_model_jacobian_eval, None, ModelMeasure)
ModelMeasure.model_jacobian = new_instancemethod(_model_measure.ModelMeasure_model_jacobian, None, ModelMeasure)
ModelMeasure.model_jacobian_x = new_instancemethod(_model_measure.ModelMeasure_model_jacobian_x, None, ModelMeasure)
ModelMeasure._v_measurement = new_instancemethod(_model_measure.ModelMeasure__v_measurement, None, ModelMeasure)
ModelMeasure._v_measurement_error_cov = new_instancemethod(_model_measure.ModelMeasure__v_measurement_error_cov, None, ModelMeasure)
ModelMeasure._v_measurement_size = new_instancemethod(_model_measure.ModelMeasure__v_measurement_size, None, ModelMeasure)
ModelMeasure.assert_model_correct = new_instancemethod(_model_measure.ModelMeasure_assert_model_correct, None, ModelMeasure)
ModelMeasure.assert_jacobian_correct = new_instancemethod(_model_measure.ModelMeasure_assert_jacobian_correct, None, ModelMeasure)
ModelMeasure._v_model_measure_diff = new_instancemethod(_model_measure.ModelMeasure__v_model_measure_diff, None, ModelMeasure)
ModelMeasure._v_uncert_weighted_model_measure_diff = new_instancemethod(_model_measure.ModelMeasure__v_uncert_weighted_model_measure_diff, None, ModelMeasure)
ModelMeasure._v_uncert_weighted_jacobian = new_instancemethod(_model_measure.ModelMeasure__v_uncert_weighted_jacobian, None, ModelMeasure)
ModelMeasure._v_uncert_weighted_jac_inner_product = new_instancemethod(_model_measure.ModelMeasure__v_uncert_weighted_jac_inner_product, None, ModelMeasure)
ModelMeasure_swigregister = _model_measure.ModelMeasure_swigregister
ModelMeasure_swigregister(ModelMeasure)



