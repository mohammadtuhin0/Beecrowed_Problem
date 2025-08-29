n1, n2, n3, n4 = map(float, input().split())
media = (n1*2 + n2*3 + n3*4 + n4*1) / 10
print(f"Media: {media:.1f}")
if media >= 7.0:
    print("Aluno aprovado.")
elif media >= 5.0:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    exam_score = float(input())
    print(f"Nota do exame: {exam_score:.1f}")
    final_media = (media + exam_score) / 2
    if final_media >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print(f"Media final: {final_media:.1f}")