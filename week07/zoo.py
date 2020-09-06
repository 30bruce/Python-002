class Zoo(object):
    """
    动物园类
    名字属性、添加动物方法
    """
    animals = {}
    def __init__(self, name):
        self.name = name
    
    def add_animal(self, animal_inst):
        animal_id = id(animal_inst)
        if animal_id not in self.animals:
            self.animals[animal_id] = animal_inst
        else:
            raise Exception('Cannot add same animal')

        self.__dict__.update({animal_inst.__class__.__name__: 1})


class Animal(object):
    """
    动物类
    四个属性 类型、体型、性格、是否属于凶猛动物
    不允许被实例化
    """

    def __init__(self, *args, **kwargs):
        self.sound = kwargs.get('sound') 
        self.animal_type = kwargs.get('animal_type')
        self.shape = kwargs.get('shape')
        self.character = kwargs.get('character')
        raise Exception('Cannot create instance from Animal')
    
    @property
    def is_fierce(self):
        """
        体型>=中等 and 食肉类型 and 性格凶猛
        """
        return (self.shape in {"大", "中等"} 
                and self.animal_type == '食肉'
                and self.character == '凶猛')


class Cat(Animal):
    def __init__(self, name, animal_type, shape, character, sound=""):
        self.name = name
        self.animal_type = animal_type
        self.shape = shape
        self.character = character
        self.sound = sound
    
    @property
    def can_be_pet(self):
        return self.character != '凶猛'


class Dog(Animal):
    def __init__(self, name, animal_type, shape, character):
        self.animal_type = animal_type
        self.shape = shape
        self.character = character
        

if __name__ == '__main__':
    z = Zoo('时间动物园')
    cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
    z.add_animal(cat1)
    have_cat = hasattr(z, 'Cat')
    print(have_cat)
    print(hasattr(z, 'Dog'))

