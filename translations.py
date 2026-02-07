"""
Dictionary containing all text strings for the application.
Structure: {'key': {'ar': 'Arabic Text', 'en': 'English Text'}}
"""

MESSAGES = {
    # --- General & Navbar ---
    'app_name': {'ar': 'رصيد', 'en': 'Raseed'},
    'dashboard': {'ar': 'لوحة التحكم', 'en': 'Dashboard'},
    'login': {'ar': 'تسجيل الدخول', 'en': 'Login'},
    'signup': {'ar': 'حساب جديد', 'en': 'Sign Up'},
    'logout': {'ar': 'تسجيل خروج', 'en': 'Logout'},
    'lang_switch': {'ar': 'English', 'en': 'العربية'},
    'welcome': {'ar': 'أهلاً بك', 'en': 'Welcome'},
    
    # --- Landing Page ---
    'hero_title': {'ar': 'إدارتك العقارية.. أذكى وأسهل', 'en': 'Property Management.. Smarter & Easier'},
    'hero_desc': {'ar': 'نظام "رصيد" يمنحك السيطرة الكاملة على محفظتك العقارية. تابع الإيجارات، نبهات السداد، والتقارير المالية في مكان واحد آمن ومشفر.', 
                  'en': 'Raseed gives you full control over your real estate portfolio. Track rents, payment alerts, and financial reports in one secure, encrypted place.'},
    'start_now': {'ar': 'ابدأ مجاناً الآن', 'en': 'Start Now Free'},
    'go_dashboard': {'ar': 'الذهاب للوحة التحكم', 'en': 'Go to Dashboard'},
    'feat_security_title': {'ar': 'حماية وأمان', 'en': 'Security & Safety'},
    'feat_security_desc': {'ar': 'بياناتك مشفرة ومحفوظة في سيرفرات سحابية آمنة.', 'en': 'Your data is encrypted and stored on secure cloud servers.'},
    'feat_reports_title': {'ar': 'تقارير ذكية', 'en': 'Smart Reports'},
    'feat_reports_desc': {'ar': 'لوحة تحكم تفاعلية تعطيك نظرة شاملة على نسبة السداد.', 'en': 'Interactive dashboard giving you a comprehensive view of payment rates.'},
    'feat_speed_title': {'ar': 'سرعة وسهولة', 'en': 'Speed & Ease'},
    'feat_speed_desc': {'ar': 'واجهة ثنائية اللغة، دعم إكسل، وتصميم متجاوب.', 'en': 'Bilingual interface, Excel support, and responsive design.'},

    # --- Auth Pages ---
    'email': {'ar': 'البريد الإلكتروني', 'en': 'Email Address'},
    'password': {'ar': 'كلمة المرور', 'en': 'Password'},
    'full_name': {'ar': 'الاسم الكامل', 'en': 'Full Name'},
    'no_account': {'ar': 'ليس لديك حساب؟', 'en': 'No account?'},
    'have_account': {'ar': 'لديك حساب بالفعل؟', 'en': 'Already have an account?'},
    'create_account': {'ar': 'إنشاء حساب', 'en': 'Create Account'},
    'login_btn': {'ar': 'دخول للنظام', 'en': 'Login to System'},
    'login_subtitle': {'ar': 'أهلاً بك مجدداً في نظام رصيد', 'en': 'Welcome back to Raseed'},
    'signup_subtitle': {'ar': 'ابدأ إدارة عقاراتك باحترافية', 'en': 'Start managing your properties professionally'},

    # --- Dashboard ---
    'total_paid': {'ar': 'تم تحصيله', 'en': 'Total Paid'},
    'total_remaining': {'ar': 'متبقي', 'en': 'Remaining'},
    'add_tenant': {'ar': 'إضافة مستأجر جديد', 'en': 'Add New Tenant'},
    'alerts': {'ar': 'تنبيهات الدفع', 'en': 'Payment Alerts'},
    'tenant_list': {'ar': 'قائمة العقارات', 'en': 'Properties List'},
    'tenant_name': {'ar': 'المستأجر', 'en': 'Tenant'},
    'unit_name': {'ar': 'الوحدة', 'en': 'Unit'},
    'progress': {'ar': 'الإنجاز', 'en': 'Progress'},
    'actions': {'ar': 'الإجراء', 'en': 'Actions'},
    'details': {'ar': 'التفاصيل', 'en': 'Details'},
    'delete': {'ar': 'حذف', 'en': 'Delete'},
    'no_tenants': {'ar': 'لا يوجد مستأجرين حالياً', 'en': 'No tenants found'},
    
    # --- Tenant Details ---
    'financial_record': {'ar': 'السجل المالي', 'en': 'Financial Ledger'},
    'upload_excel': {'ar': 'رفع ملف إكسل', 'en': 'Upload Excel'},
    'due_date': {'ar': 'تاريخ الاستحقاق', 'en': 'Due Date'},
    'amount': {'ar': 'المبلغ', 'en': 'Amount'},
    'status': {'ar': 'الحالة', 'en': 'Status'},
    'pay': {'ar': 'سداد', 'en': 'Pay'},
    'update': {'ar': 'تحديث', 'en': 'Update'},
    'paid_done': {'ar': 'مدفوع', 'en': 'Paid'},
    'unpaid': {'ar': 'غير مدفوع', 'en': 'Unpaid'},
    'partial': {'ar': 'جزئي', 'en': 'Partial'},

    # --- Flash Messages (System Notifications) ---
    'flash_login_error': {'ar': 'البريد الإلكتروني أو كلمة المرور غير صحيحة', 'en': 'Invalid email or password'},
    'flash_email_exists': {'ar': 'البريد الإلكتروني مسجل مسبقاً', 'en': 'Email already registered'},
    'flash_tenant_added': {'ar': 'تم إضافة المستأجر بنجاح', 'en': 'Tenant added successfully'},
    'flash_tenant_exists': {'ar': 'خطأ: اسم المستأجر موجود مسبقاً', 'en': 'Error: Tenant name already exists'},
    'flash_access_denied': {'ar': 'غير مصرح لك بالوصول لهذا الملف', 'en': 'Access denied'},
    'flash_upload_success': {'ar': 'تم رفع جدول الدفعات بنجاح', 'en': 'Schedule uploaded successfully'},
    'flash_upload_error': {'ar': 'الملف لا يحتوي على الأعمدة المطلوبة', 'en': 'Invalid file format: Missing columns'},
    'flash_processing_error': {'ar': 'حدث خطأ أثناء المعالجة', 'en': 'Error processing file'},
    'flash_payment_recorded': {'ar': 'تم تسجيل الدفعة بنجاح', 'en': 'Payment recorded successfully'},
    'flash_amount_updated': {'ar': 'تم تحديث قيمة العقد', 'en': 'Contract amount updated'},
    'flash_deleted': {'ar': 'تم حذف السجل نهائياً', 'en': 'Record deleted permanently'},
}