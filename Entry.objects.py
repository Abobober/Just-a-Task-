Entry.objects.filter(body_text__icontains="Music").exclude(pub_date__lte="2011-01-01")
Entry.objects.filter(timestamp__month=4)
Entry.objects.filter(blog_name = "Technology")
Entry.objects.latest('pub_date')[10]
Entry.objects.filter(blog_name = "Art", comments_count_gte = 15)