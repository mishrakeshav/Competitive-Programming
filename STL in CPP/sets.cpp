#include<iostream>
#include<set>
#include<string>
#include<functional>
using namespace std;
/*
NOTES:
1. std::set is an Associative Container that contains a sorted set of unique objects of type Key.
2. It is usually implemented using Red-Black Tree.
3. Insertion, Removal, Search have logarithmic complexity.
4. If we want to store user defined data type in set then we will have to provide 
   compare function so that set can store them in sorted order.
5. We can pass the order of sorting while constructing set object.

BOTTOM LINE:
It store unique elements and they are stored in sorted order (A/D)
*/
class Person{
    public:
        float age;
        string name;
    bool operator < (const Person& rhs) const { return age < rhs.age; };
    bool operator > (const Person& rhs) const { return age > rhs.age; };

};

int main(){
    std::set<int> Set = {5,4,3,2,1};
    for(int i : Set){
        cout << i << endl;
    }

    set<Person, std::greater<>> persons = {{19, "Keshav"}, {20, "Jaideep"}, {21, "Kanha"}};
    for(Person p : persons){
        cout << p.age << " "<<p.name << endl;
    }
    return 0;
}