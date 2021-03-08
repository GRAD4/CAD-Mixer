#include <iostream>
#include <STEPControl_Reader.hxx>
#include <string>

using namespace std;


int main() {

STEPControl_Reader reader;
IFSelect_ReturnStatus stat = reader.ReadFile("C:\\Users\\Kelevradesktop.Kelevra-desktop\\Desktop\\Studienarbeit\\steptest.step");
IFSelect_PrintCount mode = IFSelect_ListByItem;
reader.PrintCheckLoad(false, mode);

Standard_Integer NbRoots = reader.NbRootsForTransfer();                      //Transfer whole file
Standard_Integer num = reader.TransferRoots();

Standard_Integer NbTrans = reader.TransferRoots();
TopoDS_Shape result = reader.OneShape();
TopoDS_Shape shape = reader.Shape();


cout << NbRoots << endl;
cout << NbTrans << endl;
cout << num << endl;

system("pause");

return 0;
}
