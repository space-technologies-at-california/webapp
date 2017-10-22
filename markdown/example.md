# Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse nec consectetur lorem. Vivamus imperdiet egestas eros ac sollicitudin. Nunc aliquet imperdiet lorem. Vivamus hendrerit commodo dui in congue. 

Ut faucibus urna non nisl ultrices eleifend. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Donec vitae ultrices lacus. Vestibulum sit amet maximus lectus. Cras nec magna a velit hendrerit condimentum ut vel neque. In velit purus, iaculis non rutrum et, tincidunt sit amet lacus. Praesent feugiat tortor ligula, vitae consectetur augue finibus eleifend. Maecenas iaculis rhoncus nulla sit amet pharetra.

_[Example Golden Bridge](http://www.goldengatebridge.org)_

![Figure Caption: Example Golden Bridge](img/background/cover1.jpg)

At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod maxime placeat facere possimus, omnis voluptas assumenda est, omnis dolor repellendus


1. Beatae vitae dicta sunt explicabo
2. Inventore veritatis et quasi architecto
3. Sed do eiusmod tempor incididunt
4. Accusamus et iusto odio dignissimos ducimus

**Sed risus libero, facilisis et maximus vitae, hendrerit eu turpis. Phasellus aliquet elit et tellus tincidunt, eget luctus ipsum dictum. Nullam tincidunt elementum tortor, eget dictum lectus laoreet eget. Nam ac odio ligula.**

> It's our challenges and obstacles that give us layers of depth and make us interesting. Are they fun when they happen? No. But they are what make us unique. And that's what I know for sure... I think.

Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. 

---

# Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt.

- Beatae vitae dicta sunt explicabo
- Inventore veritatis et quasi architecto
- Sed do eiusmod tempor incididunt
- Accusamus et iusto odio dignissimos ducimus


Vestibulum semper, enim nec `malesuada aliquam`, justo est luctus metus, eu efficitur ex sapien sed diam. Vivamus fringilla massa a erat hendrerit consectetur. `Nam purus dolor`, sagittis sit amet placerat semper, convallis id odio. 

```python
def build_model(cropping_box=((70,25), (0,0)), input_shape=(160,320,3)):
    model = Sequential()
    model.add(Cropping2D(cropping=cropping_box))
    model.add(Lambda(lambda x: x / 255.0 - 0.5, input_shape=input_shape))
    model.add(Convolution2D(24, 5, 5, subsample=(2,2), activation="elu"))
    model.add(Convolution2D(64, 3, 3, activation="elu"))
    keep_prob = 0.5
    model.add(Dropout(keep_prob))
    model.add(Flatten())
    model.add(Dense(100))
    model.add(Activation("elu"))
    model.add(Dropout(keep_prob))
    model.add(Dense(1))
    return model
```

Donec sollicitudin dui eu leo mattis, nec euismod sem finibus. Pellentesque id quam ligula. Nam consectetur elementum euismod. Ut id magna odio. Nulla suscipit enim id tincidunt
