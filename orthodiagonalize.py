def convert_to_float(input_row):
    output_row = []
    for i in input_row:
        if("/" in i):
            split_res = i.split("/")
            floatable = float(split_res[0])/float(split_res[1])
            output_row.append(floatable)
        else:
            output_row.append(float(i))
    return output_row
    
def find_eigenvalues(matrix):
    try:
        if len(matrix) != 2 or len(matrix[0]) != 2 or len(matrix[1]) != 2:
            raise ValueError("Input matrix must be a 2x2 matrix")

        a, b, c, d = matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1]

        discriminant = (a + d)**2 - 4 * (a * d - b * c)

        if discriminant >= 0:
            eigenvalue1 = (a + d + discriminant**0.5) / 2
            eigenvalue2 = (a + d - discriminant**0.5) / 2
            return eigenvalue1, eigenvalue2
        else:
            real_part = (a + d) / 2
            imaginary_part = abs(discriminant)**0.5 / 2
            eigenvalue1 = complex(real_part, imaginary_part)
            eigenvalue2 = complex(real_part, -imaginary_part)
            return eigenvalue1, eigenvalue2

    except Exception as e:
        return print("Error: ",str(e))
def get_ortho_denominator(vector):
    return vector[0]*vector[0] + vector[1]*vector[1]
    
print("Ortho Diagonalize A=PDP^T=PDP^-1:")
print("Enter matrix comma separated 2 per row")
parent_matrix = []
input_matrix_r1 = convert_to_float((input()).split(","))
input_matrix_r2 = convert_to_float((input()).split(","))
parent_matrix.append(input_matrix_r1)
parent_matrix.append(input_matrix_r2)
eigenvals = find_eigenvalues(parent_matrix)
print(eigenvals)
eigenprep1 = []
eigenprep2 = []
eigenprep1.append([parent_matrix[0][0]-eigenvals[0],parent_matrix[0][1]])
eigenprep1.append([parent_matrix[1][0],parent_matrix[1][1]-eigenvals[0]])
eigenprep2.append([parent_matrix[0][0]-eigenvals[1],parent_matrix[0][1]])
eigenprep2.append([parent_matrix[1][0],parent_matrix[1][1]-eigenvals[1]])
print("Find eigenvectors for each eigenvalue")
print("Eigenprep for value ",eigenvals[0])
print(eigenprep1)
print("Eigenprep for value ",eigenvals[1])
print(eigenprep2)
print("Enter rrefed solution from the eigenprep as a scaled vector for eigenvalue  ",eigenvals[0])
vector_1 = convert_to_float((input()).split(","))
denom1 = get_ortho_denominator(vector_1)
print("Matrix P:")
print("For eigval ", eigenvals[0]," [ ",vector_1[0],"/sqrt, ",denom1,",",vector_1[1],"/sqrt, ",denom1)

print("Enter rrefed solution from the eigenprep as a scaled vector for eigenvalue  ",eigenvals[1])
vector_2 = convert_to_float((input()).split(","))
denom2 = get_ortho_denominator(vector_2)
print("For eigval ", eigenvals[1]," [ ",vector_2[0],"/sqrt, ",denom2,",",vector_2[1],"/sqrt, ",denom2)
print("Any key")
input()
d_matrix = []
d_r1 = []
d_r2 = []
d_r1.append(eigenvals[0])
d_r1.append(0)
d_r2.append(0)
d_r2.append(eigenvals[1])
d_matrix.append(d_r1)
d_matrix.append(d_r2)
print("D matrix:")
print(d_matrix)
