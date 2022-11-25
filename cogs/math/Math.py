from nextcord.ext import commands
import nextcord
import random
import math

class Math(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @nextcord.slash_command(name="add", description="Add two numbers")
  async def add(self, inter: nextcord.Interaction, num1: int, num2: int):
    embed = nextcord.Embed(title=f"{num1} + {num2} = {num1+num2}")
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="subtract", description="Subtract two numbers")
  async def subtract(self, inter: nextcord.Interaction, num1: int, num2: int):
    embed = nextcord.Embed(title=f"{num1} - {num2} = {num1-num2}")
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="multiply", description="Multiply two numbers")
  async def multiply(self, inter: nextcord.Interaction, num1: int, num2: int):
    embed = nextcord.Embed(title=f"{num1} * {num2} = {num1*num2}")
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="divide", description="Divide two numbers")
  async def divide(self, inter: nextcord.Interaction, num1: int, num2: int):
    embed = nextcord.Embed(title=f"{num1} / {num2} = {num1/num2}")
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="power", description="Raise a number to a power")
  async def power(self, inter: nextcord.Interaction, num1: int, num2: int):
    embed = nextcord.Embed(title=f"{num1} ^ {num2} = {num1**num2}")
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="sqrt", description="Get the square root of a number")
  async def sqrt(self, inter: nextcord.Interaction, num1: int):
    embed = nextcord.Embed(title=f"sqrt({num1}) = {math.sqrt(num1)}")
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="cbrt", description="Get the cube root of a number")
  async def cbrt(self, inter: nextcord.Interaction, num1: int):
    embed = nextcord.Embed(title=f"cbrt({num1}) = {math.cbrt(num1)}")
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="root", description="Get root of a number")
  async def root(self, inter: nextcord.Interaction, num1: int, num2: int):
    embed = nextcord.Embed(title=f"{num1} root {num2} = {num1**(1/num2)}")
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="log", description="Get the log of a number")
  async def log(self, inter: nextcord.Interaction, num1: int, num2: int):
    embed = nextcord.Embed(title=f"log({num1}) base {num2} = {math.log(num1, num2)}")
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="e", description="Get e")
  async def e(self, inter: nextcord.Interaction):
    embed = nextcord.Embed(title=f"e = {math.e}")
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="log10", description="Get the log base 10 of a number")
  async def log10(self, inter: nextcord.Interaction, num1: int):
    embed = nextcord.Embed(title=f"log10({num1}) = {math.log10(num1)}")
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="log2", description="Get the log base 2 of a number")
  async def log2(self, inter: nextcord.Interaction, num1: int):
    embed = nextcord.Embed(title=f"log2({num1}) = {math.log2(num1)}")
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="logb", description="Get the log of a number with a custom base")
  async def logb(self, inter: nextcord.Interaction, num1: int, base: int):
    embed = nextcord.Embed(title=f"log({num1}) base {base} = {math.log(num1, base)}")
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="sin", description="Get the sine of a number")
  async def sin(self, inter: nextcord.Interaction, num1: int):
    embed = nextcord.Embed(title=f"sin({num1}) = {math.sin(num1)}")
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="cos", description="Get the cosine of a number")
  async def cos(self, inter: nextcord.Interaction, num1: int):
    embed = nextcord.Embed(title=f"cos({num1}) = {math.cos(num1)}")
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="tan", description="Get the tangent of a number")
  async def tan(self, inter: nextcord.Interaction, num1: int):
    embed = nextcord.Embed(title=f"tan({num1}) = {math.tan(num1)}")
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="asin", description="Get the arcsine of a number")
  async def asin(self, inter: nextcord.Interaction, num1: int):
    embed = nextcord.Embed(title=f"asin({num1}) = {math.asin(num1)}")
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="acos", description="Get the arccosine of a number")
  async def acos(self, inter: nextcord.Interaction, num1: int):
    embed = nextcord.Embed(title=f"acos({num1}) = {math.acos(num1)}")
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="atan", description="Get the arctangent of a number")
  async def atan(self, inter: nextcord.Interaction, num1: int):
    embed = nextcord.Embed(title=f"atan({num1}) = {math.atan(num1)}")
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="atan2", description="Get the arctangent of two numbers")
  async def atan2(self, inter: nextcord.Interaction, num1: int, num2: int):
    embed = nextcord.Embed(title=f"atan2({num1}, {num2}) = {math.atan2(num1, num2)}")
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="hypot", description="Get the hypotenuse of two numbers")
  async def hypot(self, inter: nextcord.Interaction, num1: int, num2: int):
    embed = nextcord.Embed(title=f"hypot({num1}, {num2}) = {math.hypot(num1, num2)}")
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="degrees", description="Convert radians to degrees")
  async def degrees(self, inter: nextcord.Interaction, num1: int):
    embed = nextcord.Embed(title=f"degrees({num1}) = {math.degrees(num1)}")
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="radians", description="Convert degrees to radians")
  async def radians(self, inter: nextcord.Interaction, num1: int):
    embed = nextcord.Embed(title=f"radians({num1}) = {math.radians(num1)}")
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="pi", description="Get the value of pi")
  async def pi(self, inter: nextcord.Interaction):
    embed = nextcord.Embed(title=f"pi = {math.pi}")
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="e", description="Get the value of e")
  async def e(self, inter: nextcord.Interaction):
    embed = nextcord.Embed(title=f"e = {math.e}")
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="tau", description="Get the value of tau")
  async def tau(self, inter: nextcord.Interaction):
    embed = nextcord.Embed(title=f"tau = {math.tau}")
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="isclose", description="Check if two numbers are close")
  async def isclose(self, inter: nextcord.Interaction, num1: int, num2: int):
    embed = nextcord.Embed(title=f"isclose({num1}, {num2}) = {math.isclose(num1, num2)}")
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="isfinite", description="Check if a number is finite")
  async def isfinite(self, inter: nextcord.Interaction, num1: int):
    embed = nextcord.Embed(title=f"isfinite({num1}) = {math.isfinite(num1)}")
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="isinf", description="Check if a number is infinite")
  async def isinf(self, inter: nextcord.Interaction, num1: int):
    embed = nextcord.Embed(title=f"isinf({num1}) = {math.isinf(num1)}")
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="exp", description="Get the exponential of a number")
  async def exp(self, inter: nextcord.Interaction, num1: int):
    embed = nextcord.Embed(title=f"exp({num1}) = {math.exp(num1)}")
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="isnan", description="Check if a number is not a number")
  async def isnan(self, inter: nextcord.Interaction, num1: int):
    embed = nextcord.Embed(title=f"isnan({num1}) = {math.isnan(num1)}")
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="ldexp", description="Get the mantissa and exponent of a number")
  async def ldexp(self, inter: nextcord.Interaction, num1: int, num2: int):
    embed = nextcord.Embed(title=f"ldexp({num1}, {num2}) = {math.ldexp(num1, num2)}")
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="modf", description="Get the fractional and integer parts of a number")
  async def modf(self, inter: nextcord.Interaction, num1: int):
    embed = nextcord.Embed(title=f"modf({num1}) = {math.modf(num1)}")
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="isqrt", description="Get the integer square root of a number")
  async def isqrt(self, inter: nextcord.Interaction, num1: int):
    embed = nextcord.Embed(title=f"isqrt({num1}) = {math.isqrt(num1)}")
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="perm", description="Get the number of permutations of a number")
  async def perm(self, inter: nextcord.Interaction, num1: int, num2: int):
    embed = nextcord.Embed(title=f"perm({num1}, {num2}) = {math.perm(num1, num2)}")
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="expm1", description="Get the exponential of a number minus 1")
  async def expm1(self, inter: nextcord.Interaction, num1: int):
    embed = nextcord.Embed(title=f"expm1({num1}) = {math.expm1(num1)}")
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="sinh", description="Get the hyperbolic sine of a number")
  async def sinh(self, inter: nextcord.Interaction, num1: int):
    embed = nextcord.Embed(title=f"sinh({num1}) = {math.sinh(num1)}")
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="cosh", description="Get the hyperbolic cosine of a number")
  async def cosh(self, inter: nextcord.Interaction, num1: int):
    embed = nextcord.Embed(title=f"cosh({num1}) = {math.cosh(num1)}")
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="tanh", description="Get the hyperbolic tangent of a number")
  async def tanh(self, inter: nextcord.Interaction, num1: int):
    embed = nextcord.Embed(title=f"tanh({num1}) = {math.tanh(num1)}")
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="asinh", description="Get the inverse hyperbolic sine of a number")
  async def asinh(self, inter: nextcord.Interaction, num1: int):
    embed = nextcord.Embed(title=f"asinh({num1}) = {math.asinh(num1)}")
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="acosh", description="Get the inverse hyperbolic cosine of a number")
  async def acosh(self, inter: nextcord.Interaction, num1: int):
    embed = nextcord.Embed(title=f"acosh({num1}) = {math.acosh(num1)}")
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="atanh", description="Get the inverse hyperbolic tangent of a number")
  async def atanh(self, inter: nextcord.Interaction, num1: int):
    embed = nextcord.Embed(title=f"atanh({num1}) = {math.atanh(num1)}")
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="abs", description="Get the absolute value of a number")
  async def abs(self, inter: nextcord.Interaction, num1: int):
    embed = nextcord.Embed(title=f"abs({num1}) = {math.fabs(num1)}")
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="ceil", description="Get the ceiling of a number")
  async def ceil(self, inter: nextcord.Interaction, num1: int):
    embed = nextcord.Embed(title=f"ceil({num1}) = {math.ceil(num1)}")
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="floor", description="Get the floor of a number")
  async def floor(self, inter: nextcord.Interaction, num1: int):
    embed = nextcord.Embed(title=f"floor({num1}) = {math.floor(num1)}")
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="trunc", description="Get the truncated value of a number")
  async def trunc(self, inter: nextcord.Interaction, num1: int):
    embed = nextcord.Embed(title=f"trunc({num1}) = {math.trunc(num1)}")
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="copysign", description="Get the value of a number with the sign of another number")
  async def copysign(self, inter: nextcord.Interaction, num1: int, num2: int):
    embed = nextcord.Embed(title=f"copysign({num1}, {num2}) = {math.copysign(num1, num2)}")
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="sign", description="Get the sign of a number")
  async def sign(self, inter: nextcord.Interaction, num1: int):
    embed = nextcord.Embed(title=f"sign({num1}) = {math.copysign(1, num1)}")
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="fmod", description="Get the remainder of a division")
  async def fmod(self, inter: nextcord.Interaction, num1: int, num2: int):
    embed = nextcord.Embed(title=f"fmod({num1}, {num2}) = {math.fmod(num1, num2)}")
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="fsum", description="Get the sum of a list of numbers")
  async def fsum(self, inter: nextcord.Interaction, num1: int, num2: int, num3: int, num4: int, num5: int):
    embed = nextcord.Embed(title=f"fsum({num1}, {num2}, {num3}, {num4}, {num5}) = {math.fsum([num1, num2, num3, num4, num5])}")
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="gcd", description="Get the greatest common divisor of a list of numbers")
  async def gcd(self, inter: nextcord.Interaction, num1: int, num2: int, num3: int, num4: int, num5: int):
    embed = nextcord.Embed(title=f"gcd({num1}, {num2}, {num3}, {num4}, {num5}) = {math.gcd(num1, num2, num3, num4, num5)}")
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="lcm", description="Get the least common multiple of a list of numbers")
  async def lcm(self, inter: nextcord.Interaction, num1: int, num2: int, num3: int, num4: int, num5: int):
    embed = nextcord.Embed(title=f"lcm({num1}, {num2}, {num3}, {num4}, {num5}) = {math.lcm(num1, num2, num3, num4, num5)}")
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="max", description="Get the maximum of a list of numbers")
  async def max(self, inter: nextcord.Interaction, num1: int, num2: int):
    embed = nextcord.Embed(title=f"max({num1}, {num2}) = {max(num1, num2)}")
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="min", description="Get the minimum of a list of numbers")
  async def min(self, inter: nextcord.Interaction, num1: int, num2: int):
    embed = nextcord.Embed(title=f"min({num1}, {num2}) = {min(num1, num2)}")
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="factorial", description="Get the factorial of a number")
  async def factorial(self, inter: nextcord.Interaction, num1: int):
    embed = nextcord.Embed(title=f"{num1}! = {math.factorial(num1)}")
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="random", description="Get a random number between two numbers")
  async def random(self, inter: nextcord.Interaction, num1: int, num2: int):
    embed = nextcord.Embed(title=f"Random number between {num1} and {num2}: {random.randint(num1, num2)}")
    await inter.response.send_message(embed=embed)

def setup(bot):
  bot.add_cog(Math(bot))