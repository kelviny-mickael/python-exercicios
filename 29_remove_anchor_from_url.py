# Complete a função/método para que retorne a URL com tudo o que estiver após a âncora ( #) removido.
# Exemplos:
# "www.codewars.com#about" --> "www.codewars.com".
# "www.codewars.com?page=1" -->"www.codewars.com?page=1".

def remove_url_anchor(url):
    value_position = url.index('#')

    return url[0:value_position]

print(remove_url_anchor('www.codewars.com#about'))
print(remove_url_anchor('www.youtube.com#home'))
print(remove_url_anchor('www.codewars.com/katas/?page=1#about'))