import os,sys
import pytest
import yaml
from pythoncode.calculator import Calculator

# print(sys.path)

def get_datas():
    with open(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'datas/datas_ymm.yml'),encoding='utf-8') as f:
        datas = yaml.safe_load(f)
        return datas
        # return out_of_index_datas,boundary_effective_value_datas,all_positive_integer_datas,negative_postive_integer_float_datas,Invalid_character_datas
print(get_datas())

class TestCase:
    datas = get_datas()
    out_of_index_datas = datas['add']['out_of_index']
    boundary_effective_value_datas = datas['add']['boundary_effective_value']
    all_positive_integer_datas = datas['add']['all_positive_integer']
    negative_postive_integer_float_datas = datas['add']['negative_postive_integer_float']
    Invalid_character_datas = datas['add']['Invalid_character']
    out_of_index_div_datas = datas['div']['out_of_index']
    boundary_effective_value_div_datas = datas['div']['boundary_effective_value']
    all_positive_integer_div_datas = datas['div']['all_positive_integer']
    negative_postive_integer_float_div_datas = datas['div']['negative_postive_integer_float']
    Invalid_character_div_datas = datas['div']['Invalid_character']

    def setup_class(self):
        self.cal = Calculator()

    # @pytest.mark.skip
    @pytest.mark.parametrize('a,b,expected',out_of_index_datas['datas'],ids=out_of_index_datas['ids'])
    def test_add_out_of_index(self,a,b,expected):
        assert  self.cal.add(a,b) == expected

    # @pytest.mark.skip
    @pytest.mark.parametrize('a,b,expected', boundary_effective_value_datas['datas'],ids=boundary_effective_value_datas['ids'])
    def test_add_boundary_effective_value(self,a,b,expected):
        assert  self.cal.add(a,b) == expected

    # @pytest.mark.skip
    @pytest.mark.parametrize('a,b,expected', all_positive_integer_datas['datas'],ids=all_positive_integer_datas['ids'])
    def test_add_all_positive_integer(self,a,b,expected):
        assert  self.cal.add(a,b) == expected

    # @pytest.mark.skip
    @pytest.mark.parametrize('a,b,expected', negative_postive_integer_float_datas['datas'],ids=negative_postive_integer_float_datas['ids'])
    def test_add_negative_postive_integer_float(self,a,b,expected):
        assert  self.cal.add(a,b) == expected

    # @pytest.mark.skip
    @pytest.mark.parametrize('a,b,expected', Invalid_character_datas['datas'],ids=Invalid_character_datas['ids'])
    def test_add_Invalid_character(self,a,b,expected,module_fixture):
        with pytest.raises(eval(expected)) :
            self.cal.add(a,b)

    @pytest.mark.parametrize('a,b,expected',out_of_index_div_datas['datas'],ids=out_of_index_div_datas['ids'])
    def test_div_out_of_index(self,a,b,expected):
        assert  self.cal.div(a,b) == expected

    @pytest.mark.parametrize('a,b,expected', boundary_effective_value_div_datas['datas'],ids=boundary_effective_value_div_datas['ids'])
    def test_div_boundary_effective_value(self,a,b,expected):
        assert  self.cal.div(a,b) == expected

    @pytest.mark.parametrize('a,b,expected', all_positive_integer_div_datas['datas'],ids=all_positive_integer_div_datas['ids'])
    def test_div_all_positive_integer(self,a,b,expected):
        assert  self.cal.div(a,b) == expected

    @pytest.mark.parametrize('a,b,expected', negative_postive_integer_float_div_datas['datas'],ids=negative_postive_integer_float_div_datas['ids'])
    def test_div_negative_postive_integer_float(self,a,b,expected):
        assert  round(self.cal.div(a,b),2) == expected

    @pytest.mark.parametrize('a,b,expected', Invalid_character_div_datas['datas'],ids=Invalid_character_div_datas['ids'])
    def test_div_Invalid_character(self,a,b,expected,module_fixture):
        with pytest.raises(eval(expected)) :
            self.cal.div(a,b)

