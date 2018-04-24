#include <iostream>
#include<algorithm> // for copy()
#include<vector>

using namespace std;

int main () {

//CREAR FUNCION
    int nT = 700;

    double dt = 0.001;
    double c = 1.0;
    
    //Rango 
    double cx = -2.0;
    double L = 2.0;

    double dx = 2.0/80.0;

    int nX = (L-cx)/dx +1;


    //U es para Ui y j
    vector<double> U(nX);
    //Uf (futuro) es para Ui y j+1
    vector<double> Uf(nX);
    vector<double> X(nX);


    //Creacion de X
    for(int i=0; i<nX;i++){
         X[i] = cx;
	 cx += dx;
  
        //cout << cx << endl;
    }

    //Definir las condiciones iniciales
    for(int i=0; i<nX;i++){
        if(X[i]<0.5 and X[i]>-0.5){
	    U[i] = 0.5;
            Uf[i] = 0.5;
	}
    	else{
            U[i] = 0.0;
	    Uf[i] = 0.0;
    	}
     //Condicion inicial
      //cout << X[i] <<  " "<< U[i] << endl;
    }


    //Generar recorrido
    for(int i=0; i<nT;i++){
        for(int k=1; k<(nX-1);k++){
            Uf[k] = U[k] - c*(dt/dx)*(U[k]-U[k-1]);
            if(i%100 == 0){
	    cout << X[k] <<  " " << Uf[k] << endl;
            }
        }
        copy(Uf.begin(), Uf.end(), U.begin());
    }

}
