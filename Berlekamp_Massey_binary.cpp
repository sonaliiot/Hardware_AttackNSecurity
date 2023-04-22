/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, PHP, Ruby,
C#, OCaml, VB, Perl, Swift, Prolog, Javascript, Pascal, HTML, CSS, JS
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>
#include <vector>
#include<iostream>
using namespace std;
// Implementation of Berlekamp-Massey algorithm for calculating linear 
// complexity of binary sequence
// s = byte array with binary sequence
// returns Length of LFSR with smallest length which generates s
// for an example: int L=BerlekampMassey(new byte[] {1,0,1,0,1,1,1,0,1,0})
//        reference: "Handbook of Applied Cryptography", p201

int BerlekampMassey(vector<int> s)
{
	int L, N, m, d;
	int n = s.size();
	vector<int> c(n);
	vector<int> b(n);
	vector<int> t(n);
	// byte[] c=new byte[n];
	// byte[] b=new byte[n];
	// byte[] t=new byte[n];

	//Initialization
	b[0] = c[0] = 1;
	N = L = 0;
	m = -1;

	//Algorithm core
	while (N<n)
	{
		d = s[N];
		for (int i = 1; i <= L; i++){
			d ^= c[i] & s[N - i];
			cout << c[i] << "&" << s[N - i] << "^ ";
			//cout << "(c["<<i<<"]&s["<<N<<"-"<<i<<"])^ ";
		}           //(d+=c[i]*s[N-i] mod 2)
		cout << endl;
		if (d == 1)
		{
			t = c;    //T(D)<-C(D)
			for (int i = 0; (i + N - m)<n; i++){
				c[i + N - m] ^= b[i];
				cout << "N=" << N << " i=" << i << " ";
				for (int i = 0; i<c.size(); i++)
					cout << c[i] << " ";
				cout << endl;
			}
			cout << "N=" << N << " ";
			for (int i = 0; i<c.size(); i++)
				cout << c[i] << " ";
			cout << endl;
			if (L <= (N >> 1))
			{
				L = N + 1 - L;
				m = N;
				b = t;    //B(D)<-T(D)
			}
		}
		N++;
	}
	for (int i = 0; i<c.size(); i++)
		cout << c[i] << " ";
	cout << endl;
	cout << "Length: " << L << endl;
	return L;

}

int main()
{
	// printf("Hello World");
	//	vector<int> s{ 1, 0, 1, 0, 1, 1, 1, 0, 1, 0 };
	vector<int> s{ 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0 }; //1+x+x^4 with seed=[0, 1, 0,0]

	BerlekampMassey(s);
	return 0;
}
