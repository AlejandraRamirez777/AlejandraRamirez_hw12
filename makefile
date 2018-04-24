graph.png : advection.txt
	python Ar_graph.py

advection.txt : ./a.out
	./a.out > advection.txt

./a.out :
	g++ AR_advection.cpp
