#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <ctime>
#include <algorithm>

using namespace std;

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
		w[i] += (double)od.y * od.x[i];
}

void do_update(double w[],vector<one_data> data,int &total){
	for(int i = 0; i < data.size();i++){
		if(is_mistake(w,data[i])){
			add_to_w(w,data[i]);
			total --;
		}
		if(total == 0)
			break;
	}
}

void do_once(double w[],vector<one_data> data);

void shuffle_data(vector<one_data> &data){
	srand(time(NULL));
	for(int i = 0; i < data.size(); i ++)
		swap(data[i],data[rand()% (data.size() - i) + i]);
}

int main(){
	ifstream file_train("18.train");
	vector<one_data> data;

	string file_line;
	while(getline(file_train,file_line)){
		stringstream ss;
		ss.str(file_line);
		one_data dat;
		dat.x[0] = 1;
		ss >> dat.x[1] >> dat.x[2] >> dat.x[3] >> dat.x[4] >> dat.y;
		data.push_back(dat);
	}
	int error_rate[100] = {0};
	double aver = 0.0;
	for(int i = 0; i < 2000; i++){
//		cout << "run " << i+1 << endl;
		shuffle_data(data);
		double w[5] = {0,0,0,0,0};
		do_once(w,data); //with 50 update
		ifstream file_test("18.test");
		vector<one_data> data;

		string file_line;
		int error_num = 0;

		while(getline(file_test,file_line)){
			stringstream ss2;
			ss2.str(file_line);
			one_data dat;
			dat.x[0] = 1;
			ss2 >> dat.x[1] >> dat.x[2] >> dat.x[3] >> dat.x[4] >> dat.y;
			if(is_mistake(w,dat))
				error_num ++;
		}
		error_rate[error_num / 5] ++;

//		cout << ((double) error_num)  / 500.0 <<endl;
		aver += error_num;
	}
	cout << aver / (2000.0*500.0) <<endl;

	for(int i =0; i < 100; i++){
		cout << error_rate[i] <<endl;
	}
//	cout << total_up/2000 <<endl;

	return 0;
}

void do_once(double w[],vector<one_data> data){
	int total = 100;
	while(contain_mistake(w,data)){
		do_update(w,data,total);
		if(total <= 0)
			break;
	}
}
