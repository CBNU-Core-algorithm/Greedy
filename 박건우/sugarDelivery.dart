import 'dart:io';

void main() {
  var n = num.parse(stdin.readLineSync()!);
  var pack = 0;

  while (n >= 0) {
    if (n % 5 == 0) {
      pack += n ~/ 5;
      print(pack);
      return;
    }
    n -= 3;
    pack++;
  }
  print('-1');
}