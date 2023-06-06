"""Tests for substitute function."""
import filecmp
import unittest

from substitute import substitute


class TestSubstitute(unittest.TestCase):
  """TestCase subclass for testing substitute script."""

  def setUp(self):
      """Pretest setup, executes before every test."""
      pass

  def tearDown(self):
      """Posttest teardown, executes after every test."""
      pass

  def test_input_file_not_found_error(self):
      """Test Input File not found error"""
      with self.assertRaises(FileNotFoundError) as context:
        substitute.substitute("/no/such/path", 1, "/no/such/output_path")

  def test_output_file_not_found_error(self):
      """Test Output File not found error"""
      with self.assertRaises(FileNotFoundError) as context:
        substitute.substitute("./testdata/input.json", 1, "/no/such/output_path")

  def test_success(self):
      """Test successful subsitution"""
      substitute.substitute("./testdata/input.json", 3, "./testdata/output.json")
      self.assertTrue(filecmp.cmp("./testdata/output.json", "./testdata/output_success_ref.json"))
