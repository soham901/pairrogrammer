import 'package:flutter/material.dart';

class UserData {
  final String name;
  final String email;

  UserData({required this.name, required this.email});

  factory UserData.fromJson(Map<String, dynamic> json) {
    return UserData(
      name: json['name'],
      email: json['email'],
    );
  }
}

class AuthProvider with ChangeNotifier {
  UserData? _userData;
  String? _token;
  bool _isLoggedIn = false;

  UserData? get userData => _userData;
  String? get token => _token;
  bool get isLoggedIn => _isLoggedIn;

  // Set both token and logged in state
  void setToken(String token) {
    _token = token;
    _isLoggedIn = true;
    notifyListeners();
  }

  // Set user data after profile fetch
  void setUserData(UserData userData) {
    _userData = userData;
    notifyListeners();
  }

  // Clear all data on logout
  void logout() {
    _userData = null;
    _token = null;
    _isLoggedIn = false;
    notifyListeners();
  }
}