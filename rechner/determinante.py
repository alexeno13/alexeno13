import numpy as np

nXn = input("geben sie die nXn ein:")
nXn = int(nXn)

matrix = []

matrix_str = input("geben sie im Format Zahl Zahl ... die Zahlen ein:")
matrix = matrix_str.split(" ")

vektor_str = input("geben sie den vektor ein:")
vektor = vektor_str.split(" ")

the_vektor = np.array(vektor)

for i in range(len(matrix)):
    matrix[i] = float(matrix[i])

for i in range(len(vektor)):
    vektor[i] = float(vektor[i])

temp_matrix = []
final_matrix = []

det = 0

for i in range(0,len(matrix),nXn):
    temp_matrix.clear()
    for j in range(nXn):
        temp_matrix.append(matrix[i+j])
    final_matrix.append(temp_matrix.copy())

print(final_matrix)

m_matrix = np.array(final_matrix)

for m in range(0,nXn):
    #if m_matrix[m][m] == 0:
   #     break
    for n in range(m, nXn):
        print("n: " + str(n))
        print("m: " + str(m))
        if n+1 == nXn:
            break
        if not m_matrix[n+1][m] == 0:
            m_matrix[n+1] -= m_matrix[m] * m_matrix[n+1][m] / m_matrix[m][m]

        print(m_matrix)
    
    if m+1 == nXn:
        break
    
    #print(m_matrix[m+1][m]/m_matrix[m][m])

    
print(m_matrix)
det = 1

for n in range(0,nXn):
    det *= m_matrix[n][n]

print("det = " + str(det))


for m in range(nXn, 0, -1):
    print(m)
    for n in range(m, 0, -1):
        print("n: " + str(n))
        print("m: " + str(m))
        if n-1 < 0:
            break
        if not m_matrix[n-1][m-1] == 0:
            m_matrix[n-2] -= m_matrix[m-1] * m_matrix[n-2][m-1] / m_matrix[m-1][m-1]

        print(m_matrix)

    if m - 1 < 0:
        break

print(m_matrix)

answers = []

for i in range(0, nXn):
    answers.append(m_matrix[i][i])

final_answeres = []

for i in range(nXn):
    final_answeres.append(float(the_vektor[i]) / float(answers[i]))

print(final_answeres)


