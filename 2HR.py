a = r"[.,]+" #qotya bir , -belgisy bolu kerek
import re
print("\n".join(re.split(a, input())))