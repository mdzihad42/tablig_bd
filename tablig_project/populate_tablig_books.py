import os
import django

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tablig_project.settings')
django.setup()

from tablig.models import Book
from django.core.files.base import ContentFile

def populate():
    # Books data
    books_data = [
        {
            'title': 'ফাযায়েলে আমল (Fazail-e-Amaal)',
            'author': 'মাওলানা মুহাম্মদ যাকারিয়া কান্ধলবী (রহ.)',
            'description': 'ফাযায়েলে আমল তবলিগে জামাতের সবচেয়ে গুরুত্বপূর্ণ এবং বহুল পঠিত বই। এটি কয়েকটি খণ্ডের সমষ্টি, যার মধ্যে রয়েছে হিকায়াতে সাহাবা, ফাযায়েলে নামাজ, ফাযায়েলে কুরআন, ফাযায়েলে জিকির, ফাযায়েলে তবলিগ, ফাযায়েলে রমজান এবং ফাযায়েলে দরূদ। এর মূল উদ্দেশ্য হলো মুসলমানদের আমলের প্রতি উদ্বুদ্ধ করা এবং তাদের ঈমানি জজবা বৃদ্ধি করা।',
            'filename': 'fazail_e_amaal.pdf'
        },
        {
            'title': 'ফাযায়েলে সাদাকাত (Fazail-e-Sadaqat)',
            'author': 'মাওলানা মুহাম্মদ যাকারিয়া কান্ধলবী (রহ.)',
            'description': 'ফাযায়েলে সাদাকাত মাওলানা মুহাম্মদ যাকারিয়া কান্ধলবী (রহ.) এর সংকলিত একটি বিখ্যাত কিতাব। এই কিতাবে দান-সদকার গুরুত্ব, ফজিলত এবং কৃপণতার অপকারিতা সম্পর্কে কোরআন ও হাদীসের আলোকে বিস্তারিত আলোচনা করা হয়েছে। এটি মুমিনের অন্তরে আল্লাহর রাস্তায় খরচ করার মানসিকতা তৈরি করতে সাহায্য করে।',
            'filename': 'fazail_e_sadaqat.pdf'
        }
    ]

    # Create media directories if they don't exist
    media_root = 'media'
    pdf_dir = os.path.join(media_root, 'books_pdf')
    os.makedirs(pdf_dir, exist_ok=True)

    for data in books_data:
        # Check if book already exists
        if not Book.objects.filter(title=data['title']).exists():
            book = Book(
                title=data['title'],
                author=data['author'],
                description=data['description']
            )
            
            # Create a dummy PDF file
            dummy_content = f"Book Name: {data['title']}\nAuthor: {data['author']}\n\n{data['description']}\n\n(Sample File)".encode('utf-8')
            book.pdf_file.save(data['filename'], ContentFile(dummy_content))
            
            book.save()
            print(f"Added book: {data['filename']}") # Print filename instead of title to avoid encoding errors
        else:
            print(f"Book already exists.")

if __name__ == '__main__':
    populate()
