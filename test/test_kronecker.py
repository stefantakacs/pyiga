from pyiga.kronecker import *

def _kron2d_test(X, Y, XY):
    n = X.shape[0]

    x = np.random.rand(n**2)
    y1 = apply_kronecker((X,Y), x)
    #y2 = apply_tprod((X,Y), x.reshape(n,n))    # TODO: doesn't work for sparse
    assert abs(XY.dot(x) - y1).max() < 1e-10
    #assert abs(XY.dot(x) - y2.ravel()).max() < 1e-10

    x = np.random.rand(n**2, 1)
    assert np.allclose(XY.dot(x), apply_kronecker((X,Y), x))

    x = np.random.rand(n**2, 7)
    assert np.allclose(XY.dot(x), apply_kronecker((X,Y), x))

def test_kronecker_2d():
    X = np.random.rand(8,8)
    Y = np.random.rand(8,8)
    XY = np.kron(X, Y)
    _kron2d_test(X, Y, XY)

def test_kronecker_2d_sparse():
    n = 50
    from numpy.random import rand
    X = scipy.sparse.diags([rand(n-1), rand(n), rand(n-1)], offsets=(-1,0,1))
    Y = scipy.sparse.diags([rand(n-1), rand(n), rand(n-1)], offsets=(-1,0,1))
    XY = scipy.sparse.kron(X, Y)
    _kron2d_test(X, Y, XY)


def _kron3d_test(X, Y, Z, XYZ):
    n = X.shape[0]
    x = np.random.rand(n**3)
    y1 = apply_kronecker((X,Y,Z), x)
    #y2 = apply_tprod((X,Y,Z), x.reshape(n,n,n))    # TODO: doesn't work for sparse
    assert abs(XYZ.dot(x) - y1).max() < 1e-10
    #assert abs(XYZ.dot(x) - y2.ravel()).max() < 1e-10

    x = np.random.rand(n**3, 1)
    assert np.allclose(XYZ.dot(x), apply_kronecker((X,Y,Z), x))

    x = np.random.rand(n**3, 7)
    assert np.allclose(XYZ.dot(x), apply_kronecker((X,Y,Z), x))

def test_kronecker_3d():
    X = np.random.rand(8,8)
    Y = np.random.rand(8,8)
    Z = np.random.rand(8,8)
    XYZ = np.kron(np.kron(X, Y), Z)
    _kron3d_test(X, Y, Z, XYZ)

def test_kronecker_3d_sparse():
    n = 25
    from numpy.random import rand
    X = scipy.sparse.diags([rand(n-1), rand(n), rand(n-1)], offsets=(-1,0,1))
    Y = scipy.sparse.diags([rand(n-1), rand(n), rand(n-1)], offsets=(-1,0,1))
    Z = scipy.sparse.diags([rand(n-1), rand(n), rand(n-1)], offsets=(-1,0,1))
    XYZ = scipy.sparse.kron(scipy.sparse.kron(X, Y), Z)
    _kron3d_test(X, Y, Z, XYZ)
