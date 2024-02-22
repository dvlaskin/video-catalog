from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import redirect, render

from . import helpers
from .models import Category, VideoItem


def home(request):
    return render(request, 'index.html')


def catalog(request, category_id=None):

    category_list = Category.objects.all().order_by('OrderId')

    if category_id:
        video_list = VideoItem.objects.filter(Categories=category_id).order_by('-id')
        video_header_title = category_list.filter(id=category_id).first().Name
    else:
        video_list = VideoItem.objects.all().order_by('-id')[:10]
        video_header_title = 'Latest videos uploaded'

    # Set the number of items to display per page
    items_per_page = 3  # Adjust this value according to your needs
    paginator = Paginator(video_list, items_per_page)

    # Handle the Page Number from the Request
    page = request.GET.get('page')

    try:
        current_page = paginator.get_page(page)
    except PageNotAnInteger:
        current_page = paginator.get_page(1)  # Display the first page when the page number is not an integer
    except EmptyPage:
        current_page = paginator.get_page(paginator.num_pages)  # Display the last page when the page is out of range


    page_data = {
        'video_list': current_page,
        'category_list': category_list,
        'video_header_title': video_header_title,
        'share_video_link': helpers.get_current_site_name(request) + '/video',
        'show_search': True,
    }

    return render(request, 'catalog.html', page_data)


def search(request):

    if request.method != 'POST':
        return redirect('home')
    
    if not request.POST['search_text']:
        return redirect('home')

    if str.isspace(request.POST['search_text']):
        return redirect('home')
    
    print(f"searching {request.POST['search_text']}...")
    video_list = VideoItem.objects.filter(Title__icontains=request.POST['search_text'])

    category_list = Category.objects.all().order_by('OrderId')

    page_data = {
        'video_list': video_list,
        'category_list': category_list,
        'video_header_title': f'Search results for: {request.POST["search_text"]}',
        'share_video_link': helpers.get_current_site_name(request) + '/video',
        'show_search': True,
    }

    return render(request, 'catalog.html', page_data)


def video_link(request, video_id=None):

    try:
        video_record = VideoItem.objects.get(pk=video_id)

        page_data = {
            'video_record': video_record,
            'show_search': True,
        }

        return render(request, 'video.html', page_data)

    except VideoItem.DoesNotExist:
        print(' => video not found')
        # Handle the case where the record with the specified primary key does not exist
        return redirect('home')
