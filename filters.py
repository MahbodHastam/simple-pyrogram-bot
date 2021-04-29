from pyrogram import filters
from functions import *

async def isOn_func(_, __, ___):
  return getStatus() == 'on'
isOn = filters.create(isOn_func)

def text_filter(text):
  async def func(flt, _, query):
    return flt.text == query.text
  return filters.create(func, text=text)