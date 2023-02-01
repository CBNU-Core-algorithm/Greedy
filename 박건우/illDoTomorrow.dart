import 'dart:io';
import 'dart:math';

void main() {
  num? n = num.parse(stdin.readLineSync()!);
  List<List<num>> list = [];

  for (var i = 0; i < n; i++) {
    List<num> pair = [];
    stdin.readLineSync()!.split(' ').forEach((element) {
      pair.add(num.parse(element));
    });
    list.add(pair);
  }

  list.sort((a, b) => b[1].compareTo(a[1]));

  var playTime = list[0][1];
  for (var i = 0; i < n; i++) {
    // print(playTime);
    playTime = min(list[i][1], playTime) - list[i][0];
  }
  print(playTime);
}
