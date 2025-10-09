import numpy as np

### ===============================
### 1. BASICS: Creating arrays
### ===============================
# From Python lists
arr1 = np.array([1, 2, 3])
arr2d = np.array([[1, 2, 3], [4, 5, 6]])

# Special arrays
zeros = np.zeros((2, 3))             # 2x3 zeros
ones = np.ones((2, 3))               # 2x3 ones
full = np.full((2, 3), 7)            # fill with constant
eye = np.eye(3)                      # identity matrix
rand = np.random.rand(2, 3)          # uniform [0,1)
randn = np.random.randn(2, 3)        # standard normal
arange = np.arange(0, 10, 2)         # [0,2,4,6,8]
linspace = np.linspace(0, 1, 5)      # [0., 0.25, 0.5, 0.75, 1.]

# Info
print(arr2d.shape, arr2d.ndim, arr2d.dtype, arr2d.size)

### ===============================
### 2. INDEXING & SLICING
### ===============================
a = np.arange(10)   # [0..9]
print(a[0], a[-1])         # first, last
print(a[2:7:2])            # slicing with step
print(a[::-1])             # reversed

b = np.arange(12).reshape(3, 4)
print(b[0, 1])              # element
print(b[:, 1])              # entire column
print(b[1, :])              # entire row
print(b[::2, ::2])          # sub-sampling

# Boolean indexing
print(a[a > 5])             # filter elements
# Fancy indexing
idx = [0, 2, 4]
print(a[idx])

### ===============================
### 3. OPERATIONS
### ===============================
x = np.array([1, 2, 3])
y = np.array([10, 20, 30])

# Element-wise
print(x + y, x * y, x ** 2)

# Universal functions (ufuncs)
print(np.sqrt(x), np.exp(x), np.log(y))

# Aggregate functions
print(x.sum(), x.mean(), x.std(), x.min(), x.max())

# Axis operations
M = np.arange(1, 13).reshape(3, 4)
print(M.sum(axis=0))   # column sums
print(M.sum(axis=1))   # row sums

### ===============================
### 4. SHAPES & RESHAPING
### ===============================
arr = np.arange(8)
print(arr.reshape(2, 4))
print(arr.reshape(2, -1))   # auto-infer
print(arr.ravel())          # flatten (view)
print(arr.flatten())        # flatten (copy)
print(arr.T)                # transpose

### ===============================
### 5. STACKING & SPLITTING
### ===============================
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])

print(np.vstack([a, b]))      # vertical stack
print(np.hstack([a, b.T]))    # horizontal stack
print(np.concatenate([a, a], axis=1)) # concat along axis

# Splitting
c = np.arange(9).reshape(3, 3)
print(np.split(c, 3))         # equal splits
print(np.array_split(c, 2))   # uneven splits

### ===============================
### 6. BROADCASTING
### ===============================
a = np.array([1, 2, 3])
print(a + 5)                 # scalar → broadcast
M = np.ones((3, 3))
print(M + a)                 # 1D → 2D broadcast

### ===============================
### 7. LINEAR ALGEBRA
### ===============================
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print(A @ B)                   # matrix product
print(np.dot(A, B))            # same
print(np.linalg.inv(A))        # inverse
print(np.linalg.det(A))        # determinant
print(np.linalg.eig(A))        # eigenvalues & eigenvectors

### ===============================
### 8. RANDOM MODULE
### ===============================
print(np.random.randint(0, 10, size=(2, 3)))  # integers
print(np.random.choice([1, 2, 3], size=5))    # sample
print(np.random.permutation(10))              # shuffle

### ===============================
### 9. ADVANCED INDEXING
### ===============================
arr = np.arange(12).reshape(3, 4)
rows = np.array([0, 2])
cols = np.array([1, 3])
print(arr[rows[:, None], cols])   # pick (0,1), (0,3), (2,1), (2,3)

### ===============================
### 10. MISC / ADVANCED
### ===============================
arr = np.arange(5)
print(np.where(arr % 2 == 0, arr, -1))  # conditional replace
print(np.unique([1,2,2,3,3,3]))         # unique values
print(np.intersect1d([1,2,3],[2,3,4]))  # intersection
print(np.setdiff1d([1,2,3],[2,3,4]))    # difference

# ix_ trick (outer indexing)
x = np.array([1,2,3])
y = np.array([10,20,30])
print(np.add.outer(x, y))               # outer sum
print(x[np.ix_([0,2],[0,1])])           # combine indices

### ===============================
### 11. SAVING / LOADING
### ===============================
np.save("array.npy", arr)        # save binary
np.load("array.npy")             # load binary
np.savetxt("array.txt", arr)     # save text
np.loadtxt("array.txt")          # load text
