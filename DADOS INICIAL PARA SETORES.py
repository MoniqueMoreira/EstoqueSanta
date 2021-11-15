import pickle
produtos_s1=['Luvas de látex','Mascaras','Bisturi Elétrico','Aspirador Cirúrgico']
pickle.dump( produtos_s1, open( "s1p.pickls", "wb" ) )
quantidade_s1=[10,10,5,2]
pickle.dump( quantidade_s1, open( "s1q.pickls", "wb" ) )
codigos_s1=['cód.12','cód.13','cód.14','cód.16']
pickle.dump( codigos_s1, open( "s1c.pickls", "wb" ) )
produtos_s2=['Copos Descartáveis','Kit talheres Descartáveis','Pratos Descartáveis']
pickle.dump( produtos_s2, open( "s2p.pickls", "wb" ) )
quantidade_s2=[50,60,20]
pickle.dump( quantidade_s2, open( "s2q.pickls", "wb" ) )
codigos_s2=['cód.15','cód.17','cód.18']
pickle.dump( codigos_s2, open( "s2c.pickls", "wb" ) )
produtos_s3=['Agulhas descartáveis tamanho 22','Kit de Equipo de soro','Algodão']
pickle.dump( produtos_s3, open( "s3p.pickls", "wb" ) )
quantidade_s3=[50,30,10]
pickle.dump( quantidade_s3, open( "s3q.pickls", "wb" ) )
codigos_s3=['cód.19','cód.20','cód.21']
pickle.dump( codigos_s3, open( "s3c.pickls", "wb" ) )
produtos_s4=['Lencois para cama','Travesseiro']
pickle.dump( produtos_s4, open( "s4p.pickls", "wb" ) )
quantidade_s4=[50,50]
pickle.dump( quantidade_s4, open( "s4q.pickls", "wb" ) )
codigos_s4=['cód.22','cód.23']
pickle.dump( codigos_s4, open( "s4c.pickls", "wb" ) )
produtos_s5=['Ibuprofeno','Dipirona','Paracetamol']
pickle.dump( produtos_s5, open( "s5p.pickls", "wb" ) )
quantidade_s5=[10,30,15]
pickle.dump( quantidade_s5, open( "s5q.pickls", "wb" ) )
codigos_s5=['cód.24','cód.25','cód.26']
pickle.dump( codigos_s5, open( "s5c.pickls", "wb" ) )
produtos_geral=produtos_s1+produtos_s2+produtos_s3+produtos_s4+produtos_s5
pickle.dump( produtos_geral, open( "gp.pickls", "wb" ) )
quantidad_geral=quantidade_s1+quantidade_s2+quantidade_s3+quantidade_s4+quantidade_s5
pickle.dump( quantidad_geral, open( "gq.pickls", "wb" ) )
codigos_geral=codigos_s1+codigos_s2+codigos_s3+codigos_s4+codigos_s5
pickle.dump( codigos_geral, open( "gc.pickls", "wb" ) )

