class Pokemon:
  def __init__(self, name, level, pok_type,maximum_health, current_health):
    self.name = name
    self.level = level
    self.pok_type = pok_type
    self.maximum_health = maximum_health
    self.current_health = current_health
    self.is_knocked_out = False

  def __repr__(self):
    return "{} has been created, this is a {} type Pokemon with health {}".format(self.name, self.pok_type, self.current_health)

  def lose_health(self, value):
    self.current_health -= value
    return self.name + " has lost health and is now at " + str(self.current_health) + " health"

  def regain_health(self, value):
    if self.current_health == self.maximum_health:
      return self.name + " is at maximum health"
    elif self.current_health + value <= self.maximum_health:
      self.current_health += value
      return "{} has regained health, it is at {} health".format(self.name, self.current_health)
    else:
      self.current_health += self.maximum_health - self.current_health
      return "{} has regained health, it is at {} health".format(self.name, self.current_health)
  
  def knocked_out(self):
    if self.current_health <= 0:
      self.is_knocked_out = True
    return self.is_knocked_out

  def revive_pokemon(self):
    if self.name is knocked_out():
      regain_health(self, 30)

  def attack(self, defend_pokemon):
    attack_value = 10
    if not self.knocked_out():
      if self.pok_type == "Fire" and defend_pokemon.pok_type == "Grass":
        x = defend_pokemon.lose_health(2*attack_value)
        print("{} was attacked by {}. {}".format(defend_pokemon.name, self.name, x))
      elif self.pok_type == "Grass" and defend_pokemon.pok_type == "Fire":
        x = defend_pokemon.lose_health(attack_value//2)
        print("{} was attacked by {}. {}".format(defend_pokemon.name, self.name, x))
      elif self.pok_type == "Fire" and defend_pokemon.pok_type == "Water":
        x = defend_pokemon.lose_health(attack_value//2)
        print("{} was attacked by {}. {}".format(defend_pokemon.name, self.name, x))
      elif self.pok_type == "Water" and defend_pokemon.pok_type == "Fire":
        x = defend_pokemon.lose_health(2*attack_value)
        print("{} was attacked by {}. {}".format(defend_pokemon.name, self.name, x))
      elif self.pok_type == "Water" and defend_pokemon.pok_type == "Grass":
        x = defend_pokemon.lose_health(attack_value//2)
        print("{} was attacked by {}. {}".format(defend_pokemon.name, self.name, x))
      else:
        x = defend_pokemon.lose_health(2*attack_value)
        print("{} was attacked by {}. {}".format(defend_pokemon.name, self.name, x))
    else:
      print("{} is knocked out and cannot attack".format(self.name))

class Trainer:
  def __init__(self, name, pok_list, potions, active):
    self.name = name
    self.pok_list = pok_list
    self.potions = potions
    self.active_pok = pok_list.index(active)
    self.current_pok = pok_list[self.active_pok]

  def __repr__(self):
    return "Trainer's name is {}, he has {} pokemons and active pokemon is {}".format(self.name, len(self.pok_list), self.active_pok)

  def use_potion(self):
    x = self.current_pok.regain_health(10)
    self.potions -= 1
    print("Potion was used. {}".format(x))

  def switch_pokemon(self, pokemon):
    if not pokemon.knocked_out():
      self.active_pok = self.pok_list.index(pokemon)
      self.current_pok = self.pok_list[self.active_pok]
      print("{}'s Active pokemon changed to {}".format(self.name, self.active_pok))
    else:
      print("Pokemon is knocked out, cannot make it active")

  def attack_trainer(self, trainer):
    print("{} attacked {},".format(self.name, trainer.name))
    self.current_pok.attack(trainer.current_pok)
    
