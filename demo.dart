import 'dart:convert';
import 'package:http/http.dart' as http;

Future<void> login(String email, String password) async {
  const String url = 'http://localhost:3000/api/auth/login';

  final Map<String, dynamic> requestBody = {
    'email': email,
    'password': password,
  };

  try {
    final response = await http.post(
      Uri.parse(url),
      headers: {'Content-Type': 'application/json'},
      body: jsonEncode(requestBody),
    );

    if (response.statusCode == 200) {
      final responseData = jsonDecode(response.body);
      print('Login successful: ${responseData['token']}');
      // You can save the token or use it further in your app
    } else if (response.statusCode == 401) {
      final responseData = jsonDecode(response.body);
      print('Error: ${responseData['message']}');
    } else {
      print('Unexpected error: ${response.statusCode}');
    }
  } catch (e) {
    print('Error calling login API: $e');
  }
}
