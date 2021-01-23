import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: MatrixView(),
    );
  }
}

class MatrixView extends StatefulWidget {
  @override
  _MatrixViewState createState() => _MatrixViewState();
}

class _MatrixViewState extends State<MatrixView> {
  var someList = List.generate(3, (i) => List.generate(3, (j) => i + j));

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        body: Column(
      mainAxisAlignment: MainAxisAlignment.center,
      crossAxisAlignment: CrossAxisAlignment.center,
      children: <Widget>[
        Container(height: 300),
        Row(mainAxisAlignment: MainAxisAlignment.center, children: <Widget>[
          Row(
            children: _createMatrixRow(someList),
          ),
        ]),
        Container(height: 300),
      ],
    ));
  }

  List<Widget> _createMatrixRow(List<List<int>> list) {
    return new List<Widget>.generate(list.length, (int index) {
      return Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: _createMatrixColumn(list[index]));
    });
  }

  List<Widget> _createMatrixColumn(List<int> list) {
    return new List<Widget>.generate(list.length, (int index) {
      return TextButton(
          onPressed: null,
          child: Text(
            list[index].toString(),
            style: TextStyle(color: Colors.black87, fontSize: 32),
          ));
    });
  }
}
