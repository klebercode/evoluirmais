from django.shortcuts import render

from evoluirmais.core.forms import ContactForm, SubscriptionForm


def home(request):
    context = {}

    # contact
    if request.method == 'POST':
        if request.POST['action'] == 'contact':
            contact_form = ContactForm(request.POST, prefix='Contact')
            subscription_form_1 = SubscriptionForm(
                initial={'type': 1}, prefix='Subscription1')
            subscription_form_2 = SubscriptionForm(
                initial={'type': 2}, prefix='Subscription2')
            if contact_form.is_valid():
                contact_form.send_mail()
                context['contact_success'] = True
        elif request.POST['action'] == 'subscription1':
            subscription_form_1 = SubscriptionForm(
                request.POST, prefix='Subscription1')
            subscription_form_2 = SubscriptionForm(
                initial={'type': 2}, prefix='Subscription2')
            contact_form = ContactForm(prefix='Contact')
            if subscription_form_1.is_valid():
                subscription_form_1.save()
                subscription_form_1.send_mail()
                context['subscription_success_1'] = True
        elif request.POST['action'] == 'subscription2':
            subscription_form_1 = SubscriptionForm(
                initial={'type': 1}, prefix='Subscription1')
            subscription_form_2 = SubscriptionForm(
                request.POST, prefix='Subscription2')
            contact_form = ContactForm(prefix='Contact')
            if subscription_form_2.is_valid():
                subscription_form_2.save()
                subscription_form_2.send_mail()
                context['subscription_success_2'] = True
    else:
        contact_form = ContactForm(prefix='Contact')
        subscription_form_1 = SubscriptionForm(initial={'type': 1},
                                               prefix='Subscription1')
        subscription_form_2 = SubscriptionForm(initial={'type': 2},
                                               prefix='Subscription2')

    context['contact_form'] = contact_form
    context['subscription_form_1'] = subscription_form_1
    context['subscription_form_2'] = subscription_form_2

    return render(request, 'index.html', context)
