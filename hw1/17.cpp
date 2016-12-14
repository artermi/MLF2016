#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <ctime>
#include <algorithm>

using namespace std;
int total_up = 0;

class one_data{
	public:
	double x[5];
	int y;
};

bool is_mistake(const double w[],one_data dat){
	double k = 0;
	for(int i = 0; i < 5; i++)
		k += w[i] * dat.x[i];
//	cout << k <<' '<< dat.y << endl;
	return ((double) dat.y * k <= 0);
}

bool contain_mistake(const double w[], vector<one_data> data){
	for(int i = 0; i < data.size();i ++){
		if(is_mistake(w,data[i])){
			return true;
		}
	}
	return false;
}
void add_to_w(double w[],one_data od){
	for(int i = 0; i < 5; i++)
		w[i] += 0.25 * (double)od.y * od.x[i];
}

void do_update(double w[],vector<one_data> data,int &total){
	for(int i = 0; i < data.size();i++){
		if(is_mistake(w,data[i])){
			add_to_w(w,data[i]);
			total ++;
		}
	}
}

void do_once(double w[],vector<one_data> data, int data_count[]);

void shuffle_data(vector<one_data> &data){
	srand(time(NULL));
	for(int i = 0; i < data.size(); i ++)
		swap(data[i],data[rand()% (data.size() - i) + i]);
}

int main(){
	ifstream file("15.dat");
	vector<one_data> data;

	string file_line;
	while(getline(file,file_line)){
		stringstream ss;
		ss.str(file_line);
		one_data dat;
		dat.x[0] = 1;
		ss >> dat.x[1] >> dat.x[2] >> dat.x[3] >> dat.x[4] >> dat.y;
		data.push_back(dat);
	}
	int data_count[200] = {0};
	for(int i = 0; i < 2000; i++){
		shuffle_data(data);
		double w[5] = {0,0,0,0,0};
		do_once(w,data,data_count);
	}

/*	for(int i =0; i<200; i++){
		cout << data_count[i] <<endl;
	}
	*/
	cout << (double)total_up/2000 <<endl;

	return 0;
}

void do_once(double w[],vector<one_data> data, int data_count[]){
	int total = 0;
	while(contain_mistake(w,data)){
		do_update(w,data,total);
	}
	total_up += total;
	cout << total << endl;
}
