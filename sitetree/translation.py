from modeltranslation.translator import translator, TranslationOptions
from .utils import get_tree_item_model


class SiteTreeItemTranslationOptions(TranslationOptions):
    fields = ('title',)


translator.register(get_tree_item_model(), SiteTreeItemTranslationOptions)
