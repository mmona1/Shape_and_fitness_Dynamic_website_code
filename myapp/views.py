from django.shortcuts import render,redirect
from django.views.generic import View
from myapp.models import Post,Category




def home(request):
    # Define the category IDs for sliders, cards, and testimonials
    slider_category_id = 1
    card_category_id = 2
    testimonial_category_id = 3
    # Fetch posts for each category ID
    slider_posts = Post.objects.filter(category_id=slider_category_id)
    card_posts = Post.objects.filter(category_id=card_category_id)
    testimonial_posts = Post.objects.filter(category_id=testimonial_category_id)


    context = {
        'slider_posts': slider_posts,
        'card_posts': card_posts,
        'testimonial_posts': testimonial_posts
    }
    return render(request, 'index.html', context)



def gallery(request):
    gallery_category_id = 7 
    imagecategory_id=10
    gallery_category = Category.objects.get(id=gallery_category_id)
    gallery_posts = Post.objects.filter(category=gallery_category)
    gallery_images= Post.objects.filter(category_id=imagecategory_id)

    context = {
        'gallery_posts': gallery_posts,
        'gallery_images':gallery_images

    }
    return render(request, 'gallery.html', context)


def about(request):
   about_category_id=12
   about_id=13
   about_category=Category.objects.get(id=about_category_id)
   about_images=Post.objects.filter(category_id=about_category)
   about_posts=Post.objects.filter(category_id=about_id)
   context= {
       'about_posts':about_posts,
       'about_images':about_images
   }
   

   return render(request,'about.html', context)


def contact(request):
    contact_category_id=14
    contact_posts=Post.objects.filter(category_id=contact_category_id)
    context= {
            'contact_posts':contact_posts
    }
    return render(request,'contact.html' , context)




# def blog(request,*args,**kw):
#   return render(request,'blog.html')


# def trainer(request,*args,**kw):
#   return render(request,'trainer.html')
# def contact(request,*args,**kw):
#   return render(request,'contact.html')

























